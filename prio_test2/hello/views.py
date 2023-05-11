from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpResponse
# from .forms import Subjectform
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .models import Subject,Task
from hello.Prio_Algo import TaskSched, prioritizationAlgorithm

# Create your views here.
def index(request):
    return HttpResponse("umabot ka")

def addSub(request):
    if request.user.is_authenticated:
        
        return render(request, 'add_subject.html')
    return redirect("login")

def addTask(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        context = {'subjects': subjects, "subject_id": -1}
        return render(request, "add_task.html",context)
    return redirect("login")

def addCourseSub(request):
    if request.user.is_authenticated:
        return render(request, "add_course_subjects.html")
    return redirect("login")

def viewSched(request):
    if request.user.is_authenticated:
        tasks = []
        # TODO: uses tasks directly for now; use return value of prioritizationAlgorithm to compute actual task schedules
        tasks = prioritizationAlgorithm(Task.objects.all())
        # for task in Task.objects.all():
        #     task = TaskSched(task.taskName, None, task.dueDate)
        #     tasks.append(task)

        context = {'tasks': tasks}
        return render(request, "view_schedule.html", context)
    return redirect("login")

def addSubForm(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            subName = request.POST["subName"]
            numUnits = request.POST["numUnits"]
            subStart = request.POST["subStart"]
            subEnd = request.POST["subEnd"]
            reqName1, gradeNum1 = request.POST["reqName1"], request.POST["gradeNum1"]
            reqName2, gradeNum2 = request.POST["reqName2"], request.POST["gradeNum2"]
            reqName3, gradeNum3 = request.POST["reqName3"], request.POST["gradeNum3"]
            reqName4, gradeNum4 = request.POST["reqName4"], request.POST["gradeNum4"]
            reqName5, gradeNum5 = request.POST["reqName5"], request.POST["gradeNum5"]

            gradeNum1, gradeNum2, gradeNum3, gradeNum4, gradeNum5 = map(lambda num: num or 0,
                                            (gradeNum1, gradeNum2, gradeNum3, gradeNum4, gradeNum5))

            print(subName, numUnits, subStart, subEnd)
            addSub_details = Subject(
                subName = subName, numUnits = numUnits,
                subStart = subStart, subEnd=subEnd,
                reqName1=reqName1, gradeNum1=gradeNum1,
                reqName2=reqName2, gradeNum2=gradeNum2,
                reqName3=reqName3, gradeNum3=gradeNum3,
                reqName4=reqName4, gradeNum4=gradeNum4,
                reqName5=reqName5, gradeNum5=gradeNum5
            )
            addSub_details.save()
   
        return render(request, 'add_subject.html')
    return redirect("login")
   

def checkSub(request):
    if request.user.is_authenticated:
        all_sub = Subject.objects.all
        all_task = Task.objects.all
        return render(request,'check.html',{'all_sub':all_sub, 'all_task': all_task})     
    return redirect("login")
    

def edit_subject(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        context = {'subjects': subjects, "subject_id": -1}
        return render(request, 'edit_subject.html', context)
    return redirect("login")
    
def subject_details(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            subject_id = int(request.POST.get("subject_id", 0))
            context = {'subjects': Subject.objects.all(), "subject_id": subject_id}

            if subject_id != -1:
                subject = get_object_or_404(Subject, pk=subject_id)
                context['subject'] =  subject
            return render(request, 'edit_subject.html', context)
    return redirect("login")
    
def addTaskForm(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        context = {'subjects': subjects}
        if request.method == "POST":
            subject_id = request.POST["subject_id"]
            reqType = request.POST["reqType"]
            taskName = request.POST["taskName"]
            dueDate = request.POST["dueDate"]

            subject = get_object_or_404(Subject, pk=subject_id)
            addTask_details = Task(subName=subject,
                reqType = reqType, taskName=taskName, dueDate=dueDate
            )
            addTask_details.save()

        return render(request, 'add_task.html',context)
    return redirect("login")

    
def task_details(request):
    if request.user.is_authenticated:
        subject_id = int(request.POST.get("subject_id", 0))
        context = {'subjects': Subject.objects.all(), "subject_id": subject_id}

        if subject_id != -1:
            subject = get_object_or_404(Subject, pk=subject_id)
            context['subject'] =  subject

            subject = get_object_or_404(Subject, pk=subject_id)
            reqTypes = {
                subject.reqName1: subject.gradeNum1,
                subject.reqName2: subject.gradeNum2,
                subject.reqName3: subject.gradeNum3,
                subject.reqName4: subject.gradeNum4,
                subject.reqName5: subject.gradeNum5
            }

            context['reqTypes'] = reqTypes
        return render(request, 'add_task.html', context)
    return redirect("login")

def editSubForm(request, subject_id):
    if request.user.is_authenticated:
        subject = Subject.objects.get(id=subject_id)

        if request.method == "POST":
            subName = request.POST["subName"]
            numUnits = request.POST["numUnits"]
            subStart = request.POST["subStart"]
            subEnd = request.POST["subEnd"]
            reqName1, gradeNum1 = request.POST["reqName1"], request.POST["gradeNum1"]
            reqName2, gradeNum2 = request.POST["reqName2"], request.POST["gradeNum2"]
            reqName3, gradeNum3 = request.POST["reqName3"], request.POST["gradeNum3"]
            reqName4, gradeNum4 = request.POST["reqName4"], request.POST["gradeNum4"]
            reqName5, gradeNum5 = request.POST["reqName5"], request.POST["gradeNum5"]

            gradeNum1, gradeNum2, gradeNum3, gradeNum4, gradeNum5 = map(lambda num: num or 0,
                                            (gradeNum1, gradeNum2, gradeNum3, gradeNum4, gradeNum5))


            subject.subName = subName
            subject.numUnits = numUnits
            subject.subStart = subStart
            subject.subEnd = subEnd
            subject.reqName1, subject.gradeNum1 = reqName1, gradeNum1
            subject.reqName2, subject.gradeNum2 = reqName2, gradeNum2
            subject.reqName3, subject.gradeNum3 = reqName3, gradeNum3
            subject.reqName4, subject.gradeNum4 = reqName4, gradeNum4
            subject.reqName5, subject.gradeNum5 = reqName5, gradeNum5

            subject.save()

        subjects = Subject.objects.all()
        context = {'subjects': subjects, "subject_id": -1}
        return render(request, 'edit_subject.html', context)
    return redirect("login")
