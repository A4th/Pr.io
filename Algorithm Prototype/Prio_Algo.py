from datetime import datetime, time, timedelta

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

## Step 2. Compute absolute time remaining
# # # today = datetime.today()
today = datetime(month=4, day=26, year=2023, hour=12+6, minute=0)
for task in tasks:
    # NOTE: directly mutates task records/objects for simplicity
    task["absTime"] = task["dueDate"] - today

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
for task in tasks:
    print(task["name"])
    # NOTE: directly mutates task records/objects for simplicity
    task["remTime"] = task["absTime"]
    dueDay = task["dueDate"].date()
    dueTime = timedelta(hours=task["dueDate"].hour, minutes = task["dueDate"].minute)
    todayTime = timedelta(hours=today.hour, minutes=today.minute)

    # dueDay - today is number of days remaining, but includes dueDate itself
    # so we subtract one day to only get the days "in the middle"
    # e.g. d0 | d1 d2 d3 | d4 has 3 middle days, (4-0)-1 = 3
    wholeDays = (dueDay - today.date() - timedelta(days=1)).days
    for brk in breaks:
        # for each whole day, subtract complete duration of break
        task["remTime"] -= brk["duration"]*wholeDays

        print(todayTime, dueTime, brk["start"], brk["end"])
        # for today, only subtract time which overlaps with break time
        if (todayTime <= brk["start"]):
            delta = max(todayTime, brk["end"]) - brk["start"]
            task["remTime"] -= delta
            print("\ttoday overlap", delta)

        # for dueDate, only subtract time which overlaps with break time
        if (dueTime >= brk["end"]):
            delta = min(dueTime, brk["end"]) - brk["start"]
            task["remTime"] -= delta
            print("\tdueDate overlap", delta)
    #
    # for subjSched in subjectScheds:
    #   TODO: implement
    print()

# Sort tasks by remaining time
tasks.sort(key=lambda task: task["remTime"])
print(*tasks,sep="\n")

for task in tasks:
    print( f"[{task['subject']}]",
           task['name'],
           task['dueDate'],
           task['units'],
           task['gradeContrib'],
           str(task["remTime"]),
        sep="\t\t")
    print()


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

