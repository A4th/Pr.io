from datetime import datetime, time, timedelta
import logging
logging.basicConfig(filename='prio.log', encoding='utf-8', level=logging.DEBUG)

# range of hours per bin (difference between time of longest
# and shortest task in bin). Used for clustering
BIN_HOUR = 8

#### Test Data
tasks = [
{
    "subject": "CS 192",
    "name": "Sprint 3",
    "dueDate": datetime(month=4,day=28,year=2023,hour=9, minute=20),
    "units": 3.0,
    "gradeContrib": 3.6
},
{
    "subject": "CS 145",
    "name": "Lab Report 8",
    "dueDate": datetime(month=4,day=30,year=2023,hour=12+11, minute=59),
    "units": 4.0,
    "gradeContrib": 2
},
{
    "subject": "CS 132",
    "name": "Long Exam",
    "dueDate": datetime(month=4,day=28,year=2023,hour=12+1, minute=0),
    "units": 3.0,
    "gradeContrib": 30
},
{
    "subject": "CS 180",
    "name": "Problem Set",
    "dueDate": datetime(month=4,day=28,year=2023,hour=12+11, minute=59),
    "units": 3.0,
    "gradeContrib": 6.667
},
{
    "subject": "CS 153",
    "name": "Problem Set",
    "dueDate": datetime(month=4,day=28,year=2023,hour=12+11, minute=59),
    "units": 3.0,
    "gradeContrib": 4
},
{
    "subject": "CS 145",
    "name": "Problem Set 15",
    "dueDate": datetime(month=4,day=30,year=2023,hour=12+11, minute=59),
    "units": 4.0,
    "gradeContrib": 2
}
]


# HACK: use timedelta instead of time so that we can subtract
breaks = [
{
    "name": "Sleep",
    "start": timedelta(hours=0, minutes=0),
    "end": timedelta(hours=6, minutes=0)
},
{
    "name": "Breakfast",
    "start": timedelta(hours=6, minutes=0),
    "end": timedelta(hours=7, minutes=0)
},
{
    "name": "Lunch",
    "start": timedelta(hours=12, minutes=0),
    "end": timedelta(hours=12+1, minutes=0)
},
{
    "name": "Dinner",
    "start": timedelta(hours=12+7, minutes=0),
    "end": timedelta(hours=12+8, minutes=0)
},
]

# TODO: add subject schedules
subjectScheds = []


#### Prioritization Algorithm
## Step 1. Sort subjects by due date
tasks.sort(key=lambda task: task["dueDate"])
logging.info("Step 1. Sort subjects by due date")
logging.info("Subject\tTask\t\t\tDue Date\t\tUnits\t\t% of Grade")
for task in tasks:
    logging.info("%s\t%s\t\t%s\t%f\t%f",
        f"[{task['subject']}]",
        task['name'],
        task['dueDate'],
        task['units'],
        task['gradeContrib'],
    )
logging.info("\n")

## Step 2. compute absolute time remaining
# NOTE: "today" hardcoded to match example pre-computed values
today = datetime.today()
# today = datetime(month=4, day=26, year=2023, hour=12+6, minute=0)
for task in tasks:
    # NOTE: directly mutates task records/objects for simplicity
    task["absTime"] = task["dueDate"] - today
tasks.sort(key=lambda task: task["dueDate"])
logging.info("Step 2. compute absolute time remaining")
logging.info("Subject\tTask\t\t\tDue Date\t\tUnits\t\t% of Grade\tTime before deadline")
for task in tasks:
    logging.info("%s\t%s\t\t%s\t%f\t%f\t%s",
        f"[{task['subject']}]",
        task['name'],
        task['dueDate'],
        task['units'],
        task['gradeContrib'],
        str(task["absTime"]),
    )
logging.info("\n")


## Step 3. Subtract time needed for breaks, schedules and other necessary deductions from each absolute time.
# Preliminary step: pre-compute lengths of breaks and subject schedules
for brk in breaks:
    # NOTE: directly mutates task records/objects for simplicity
    brk["duration"] = brk["end"] - brk["start"]
for subjSched in subjectScheds:
    # NOTE: directly mutates task records/objects for simplicity
    subjSched["duration"] = subjSched["end"] - subjSched["start"]

# Sort breaks and subject schedules by start time
breaks.sort(key=lambda brk: brk["start"])
subjectScheds.sort(key=lambda subjSched: subjSched["start"])

# for each task, subtract time of break/subject Sched which overlaps with the current time up to the deadline
# in other words, subtract breaks/schedules from absolute remaining time for doing task
# NOTE: This routine assumes that breaks do NOT span multiple days (e.g. 9pm to 4am of next day are not allowed)
for task in tasks:
    # print(task["name"])
    # NOTE: directly mutates task records/objects for simplicity
    task["remTime"] = task["absTime"]
    dueDay = task["dueDate"].date()
    dueTime = timedelta(hours=task["dueDate"].hour, minutes = task["dueDate"].minute)
    todayTime = timedelta(hours=today.hour, minutes=today.minute)

    # dueDay - today is number of days remaining, but includes dueDate itself
    # so we subtract one day to only get the days "in the middle"
    # e.g. d0 | d1 d2 d3 | d4 has 3 middle days, (4-0)-1 = 3
    wholeDays = (dueDay - today.date() - timedelta(days=1)).days
    # TODO: take advantage of the sorting of breaks and subjectScheds
    # e.g. if break[n] does NOT overlap with todayTime, then neither does break[n-1] which has earlier timeslot
    # similarly, if break[n] does NOT overlap with dueTime, then neither does break[n+1] which has later timeslot
    # we don't do this for now since we need to loop over each break anyway (for subtracting breaks during wholeDays)
    for brk in breaks:
        # for each whole day, subtract complete duration of break
        task["remTime"] -= brk["duration"]*wholeDays

        # print(todayTime, dueTime, brk["start"], brk["end"])
        # for today, only subtract time which overlaps with break time
        # this only happens when todayTime is AT or BEFORE end of break
        if (todayTime <= brk["end"]):
            delta = brk["end"] - max(todayTime, brk["start"])
            task["remTime"] -= delta
            # print("\ttoday overlap", delta)

        # for dueDate, only subtract time which overlaps with break time
        # this only happens when dueDate is AFTER start of break
        if (dueTime > brk["start"]):
            delta = min(dueTime, brk["end"]) - brk["start"]
            task["remTime"] -= delta
            # print("\tdueDate overlap", delta)
    #
    # for subjSched in subjectScheds:
    #   TODO: implement
    # print()

# Sort tasks by remaining time
tasks.sort(key=lambda task: task["remTime"])
logging.info("Step 3. Subtract time needed for breaks, schedules and other necessary deductions from each absolute time.")
logging.info("Subject\tTask\t\t\tDue Date\t\tUnits\t\t% of Grade\tRemaining Time\tTime before deadline")
for task in tasks:
    logging.info("%s\t%s\t\t%s\t%f\t%f\t%s\t\t%s",
        f"[{task['subject']}]",
        task['name'],
        task['dueDate'],
        task['units'],
        task['gradeContrib'],
        str(task["remTime"]),
        str(task["absTime"]),
    )
logging.info("\n")


## Step 4. Group requirements into clusters
# Cluster tasks such that for each bin, the greatest difference in time betweem tasks is BIN_HOUR
# TODO: use faster libraries (e.g. numpy) for binning data
clusters = []
firstBinTask = None
for task in tasks:
    if (firstBinTask is None
        or (task["remTime"] - firstBinTask["remTime"]) > timedelta(hours=BIN_HOUR)):
        # create new bin for this task
        clusters.append([])
        firstBinTask = task

    clusters[-1].append(task)
# TODO: merge clusters with small number of tasks (e.g. 8 bins with one task each)

logging.info("Step 4. Group requirements into clusters")
for (i, cluster) in enumerate(clusters):
    logging.info("Cluster %s", chr(ord("A")+i))
    logging.info("Subject\tTask\t\t\tDue Date\t\tUnits\t\t% of Grade\tRemaining Time\t\t\tTime before deadline")
    for task in cluster:
        logging.info("%s\t%s\t\t%s\t%f\t%f\t%s\t\t%s",
            f"[{task['subject']}]",
            task['name'],
            task['dueDate'],
            task['units'],
            task['gradeContrib'],
            str(task["remTime"]),
            str(task["absTime"]),
        )
logging.info("\n")

## Step 5. Distribute available time per cluster fairly.
assert(len(clusters) > 2)   # For simplicity, we assume for now that there are more than one clusters
print()
for (i, cluster) in enumerate(clusters):
    if i > 0:
        clusterTime = clusters[i][0]["remTime"] - clusters[i-1][-1]["remTime"]
    else:
        clusterTime = clusters[i][-1]["remTime"]

    totalContrib = sum(map(lambda task: task["units"]*task["gradeContrib"], cluster))
    print("Cluster", chr(ord("A")+i))
    # print("Cluster", chr(ord("A")+i), clusterTime, totalContrib)
    # TODO: remove dirty hacks for aligning output columns (spaces in labels, etc.)
    print("Subject        ", "Task    ", "Due Date        ", "Units", "% of Grade", "Allocated Time", "Time before deadline", sep="\t")
    for task in cluster:
        allocTime = clusterTime * (task["units"]*task["gradeContrib"]) / totalContrib
        print( f"[{task['subject']}]",
            task['name'],
            task['dueDate'],
            task['units'],
           task['gradeContrib'], "",
            str(allocTime),
            str(task["absTime"]),
            sep="\t")
    print()

# TODO: add resting times between each tasks (student can't work for hours straight)
