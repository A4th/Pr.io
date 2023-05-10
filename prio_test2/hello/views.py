from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from .forms import Subjectform
from django.contrib import messages
from .models import Subject,Task

# Create your views here.
def index(request):
    return HttpResponse("umabot ka")

def addSub(request):
    return render(request, 'add_subject.html')

def addTask(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, "add_task.html",context)

def addCourseSub(request):
    return render(request, "add_course_subjects.html")

def viewSched(request):
    return render(request, "view_schedule.html")

def addSubForm(request):
    # print(request)
    # print("Hello World????? 1", dir(request))
    # print(request.body)
    if request.method == "POST":
        subName = request.POST["subName"]
        numUnits = request.POST["numUnits"]
        subStart = request.POST["subStart"]
        subEnd = request.POST["subEnd"]

        reqName1 = request.POST["reqName1"]
        gradeNum1 = request.POST["gradeNum1"]

        reqName2 = request.POST["reqName2"]
        gradeNum2 = request.POST["gradeNum2"]

        reqName3 = request.POST["reqName3"]
        gradeNum3 = request.POST["gradeNum3"]

        reqName4 = request.POST["reqName4"]
        gradeNum4 = request.POST["gradeNum4"]

        reqName5 = request.POST["reqName5"]
        gradeNum5 = request.POST["gradeNum5"]



        print(subName, numUnits, subStart, subEnd)
        addSub_details = Subject(
        subName=subName,
        numUnits=numUnits,
        subStart=subStart,
        subEnd=subEnd,
        reqName1=reqName1,
        gradeNum1=gradeNum1,
        reqName2=reqName2,
        gradeNum2=gradeNum2,
        reqName3=reqName3,
        gradeNum3=gradeNum3,
        reqName4=reqName4,
        gradeNum4=gradeNum4,
        reqName5=reqName5,
        gradeNum5=gradeNum5
    )

        addSub_details.save()


    
   
    return render(request, 'add_subject.html')

def checkSub(request):
    all_sub = Subject.objects.all
    return render(request,'check.html',{'all':all_sub})

def edit_subject(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'edit_subject.html', context)


def subject_details(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    context = {'subject': subject}
    return render(request, 'subject_details.html', context)

def addTaskForm(request):
    # print(request)
    # print("Hello World????? 1", dir(request))
    # print(request.body)
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    if request.method == "POST":
        reqType = request.POST["reqType"]
        taskName = request.POST["taskName"]
        dueDate = request.POST["dueDate"]

        addTask_details = Task(
        reqType = reqType,
        taskName=taskName,
        dueDate=dueDate
        )

        addTask_details.save()

    return render(request, 'add_task.html',context)


def task_details(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    context = {'subject': subject}
    return render(request, 'task_details.html', context)
