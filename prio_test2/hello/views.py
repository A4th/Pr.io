from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpResponse
# from .forms import Subjectform
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .models import *
from hello.Prio_Algo import TaskSched, prioritizationAlgorithm
from django.core.exceptions import PermissionDenied
from members.models import *

import json
from datetime import time


# String representation for days of the week
# NOTE: made global since multiple view functions need it
days = ["M", "T", "W", "Th", "F", "Sat", "Sun"]


# Create your views here.
def addSub(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if not request.user.has_perm('hello.add_subject'):
        raise PermissionDenied() 

    subjects = Subject.objects.filter(enrolee=request.user)
    # Sort subjects by start time for more efficient overlap checking
    # Sort subjects without time at the bottom since they won't lead to conflict anyway
    noTime = time(hour=23, minute=59)
    subjects = sorted(subjects, key=lambda subject: subject.subStart or noTime)

    subjects_json = {}
    for sub in subjects:
        subjects_json[sub.subName] = {"start": sub.getSubStart(), "end": sub.getSubEnd(), "subjDays": sub.subjDays}

    active_page = 'addSub'

    context = {"subjects_json": subjects_json, "days": days, "active_page": active_page}
    return render(request, 'add_subject.html', context)

def addSubForm(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.method == "POST":
        subName = request.POST["subName"]
        numUnits = request.POST["numUnits"]
        subStart = request.POST["subStart"] or None
        subEnd = request.POST["subEnd"] or None
        reqName1, gradeNum1 = request.POST["reqName1"], request.POST["gradeNum1"]
        reqName2, gradeNum2 = request.POST["reqName2"], request.POST["gradeNum2"]
        reqName3, gradeNum3 = request.POST["reqName3"], request.POST["gradeNum3"]
        reqName4, gradeNum4 = request.POST["reqName4"], request.POST["gradeNum4"]
        reqName5, gradeNum5 = request.POST["reqName5"], request.POST["gradeNum5"]
        subjDays = request.POST.getlist("subjDays")
        assert(type(subjDays) == list)

        user = request.user

        gradeNum1, gradeNum2, gradeNum3, gradeNum4, gradeNum5 = map(lambda num: num or 0,
                                        (gradeNum1, gradeNum2, gradeNum3, gradeNum4, gradeNum5))

        addSub_details = Subject(
            subName = subName, numUnits = numUnits,
            subStart = subStart, subEnd=subEnd,
            reqName1=reqName1, gradeNum1=gradeNum1,
            reqName2=reqName2, gradeNum2=gradeNum2,
            reqName3=reqName3, gradeNum3=gradeNum3,
            reqName4=reqName4, gradeNum4=gradeNum4,
            reqName5=reqName5, gradeNum5=gradeNum5,
            subjDays=subjDays, enrolee=user
        )
        addSub_details.save()

    # go back to addSub page
    return redirect("addSub")


def addTask(request, subject_id=-1):
    if not request.user.is_authenticated:
        return redirect("login")

    if not request.user.has_perm('hello.add_task'):
        raise PermissionDenied() 
    
    active_page = 'addTask'

    subjects = Subject.objects.filter(enrolee=request.user)
    context = {'subjects': subjects, "subject_id": subject_id, 'active_page':active_page}
    return render(request, "add_task.html",context)

def addTaskForm(request):
    if not request.user.is_authenticated:
        return redirect("login")

    subjects = Subject.objects.filter(enrolee=request.user)
    context = {'subjects': subjects}
    if request.method == "POST":
        subject_id = request.POST["subject_id"]
        reqType = request.POST["reqType"]
        taskName = request.POST["taskName"]
        dueDate = request.POST["dueDate"]
        notes = request.POST["taskNotes"]
        enrolee = request.user

        subject = get_object_or_404(Subject, pk=subject_id)
        addTask_details = Task(subName=subject,
            reqType = reqType, taskName=taskName, dueDate=dueDate, notes=notes, enrolee=enrolee
        )
        addTask_details.save()

        # TODO: make adding multiple tasks for same subject less cumbersome
        # # in case user wants to add more tasks for same subject
        # context["subject_id"] = subject_id

    return redirect("addTask")
    
def task_details(request):
    if not request.user.is_authenticated:
        return redirect("login")


    subject_id = int(request.POST.get("subject_id", 0))
    # Old values from previous form (e.g. when values were edited before subject is chose)
    reqType = request.POST.get("reqType", "")
    taskName = request.POST.get("taskName", "")
    dueDate = request.POST.get("dueDate", None)
    notes = request.POST.get("taskNotes", "")
    enrolee = request.user

    context = {'subjects': Subject.objects.filter(enrolee=enrolee), "subject_id": subject_id,
               "prevTaskName": taskName, "prevDueDate": dueDate, "prevNotes": notes}

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

        # Only keep previous reqType value if it is still present in new subject
        if reqType not in reqTypes:
            reqType = None

        context['reqTypes'] = reqTypes
        context['prevReqType'] = reqType

    return render(request, 'add_task.html', context)

def editTaskForm(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        task_id = request.POST["task_id"]

        task_editable_fields = {
            "taskName": request.POST["taskName"],
            "dueDate": request.POST["taskDueDate"],
            "notes": request.POST["taskNotes"]
        }

        task = Task.objects.get(id=task_id);

        for (field, value) in task_editable_fields.items():
            setattr(task, field, value)

        task.save()

    return redirect("viewSched")

def removeTaskForm(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        task_id = request.POST["task_id"]

        task = Task.objects.get(pk=task_id)
        task.delete()

    return redirect("viewSched")

def addCourseSub(request):
    if not request.user.is_authenticated:
        return redirect("login")

    degreeprogram = DegreeProgram.objects.all()
    context = {'degreeprogram': degreeprogram, "degprog_id": -1}
    return render(request, "add_course_subjects.html", context)

def addCourseSubList(request):
    if not request.user.is_authenticated:
        return redirect("login")

    degreeprogram = DegreeProgram.objects.all()
    context = {'degreeprogram': degreeprogram}
    if request.method == "POST":
        degprog_id = int(request.POST.get("degprog_id", -1))
        context['degprog_id'] = degprog_id
        if degprog_id != -1:
            subjects = DegreeProgram.objects.get(pk=degprog_id).jsonData
            subjects = list(sorted(subjects.keys()))
            context['subjects'] = subjects

    return render(request, "add_course_subjects.html", context)

def addCourseSubForm(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        degprog_id = int(request.POST.get("degprog_id"))
        subjects = request.POST.getlist("chosenSubs");

        subToUnit = DegreeProgram.objects.get(pk=degprog_id).jsonData
        for subject in subjects:
            newSub = Subject(subName=subject, numUnits= subToUnit[subject], enrolee=request.user)
            newSub.save()

    return redirect("addCourseSub")


def viewSched(request):
    if not request.user.is_authenticated:
        return redirect("login")

    tasks = Task.objects.filter(enrolee=request.user)
    taskSchedules = prioritizationAlgorithm(tasks)

    active_page = 'viewSched'
    context = {'tasks': tasks, 'taskSchedules': taskSchedules,
               'active_page': active_page,}
    return render(request, "view_schedule.html", context)


def checkSub(request):
    if not request.user.is_authenticated:
        return redirect("login")

    all_sub = Subject.objects.filter(enrolee=request.user)
    all_task = Task.objects.filter(enrolee=request.user)

    active_page = 'checkSub'

    return render(request,'check.html',{'all_sub':all_sub, 'all_task': all_task, 'active_page': active_page})
    
    
def edit_subject(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if not request.user.has_perm('hello.change_subject'):
        raise PermissionDenied() 

    subjects = Subject.objects.filter(enrolee=request.user)
    # Sort subjects by start time for more efficient overlap checking
    # Sort subjects without time at the bottom since they won't lead to conflict anyway
    noTime = time(hour=23, minute=59)
    subjects = sorted(subjects, key=lambda subject: subject.subStart or noTime)

    subjects_json = {}
    for sub in subjects:
        subjects_json[sub.subName] = {"start": sub.getSubStart(), "end": sub.getSubEnd(), "subjDays": sub.subjDays}

    active_page = 'editSub'

    context = {'subjects': subjects, "subjects_json": subjects_json, "subject_id": -1, "subject": "", "days": days, 'active_page': active_page}
    return render(request, 'edit_subject.html', context)
    
def subject_details(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        subject_id = int(request.POST.get("subject_id", 0))

        subjects = Subject.objects.filter(enrolee=request.user)
        # Sort subjects by start time for more efficient overlap checking
        # Sort subjects without time at the bottom since they won't lead to conflict anyway
        noTime = time(hour=23, minute=59)
        subjects = sorted(subjects, key=lambda subject: subject.subStart or noTime)

        subjects_json = {}
        for sub in subjects:
            subjects_json[sub.subName] = {"start": sub.getSubStart(), "end": sub.getSubEnd(), "subjDays": sub.subjDays}

        context = {'subjects': subjects, "subjects_json": subjects_json, "subject_id": subject_id, "days": days}

        if subject_id != -1:
            subject = get_object_or_404(Subject, pk=subject_id)
            context['subject'] =  subject
        return render(request, 'edit_subject.html', context)
    
def editSubForm(request, subject_id):
    if not request.user.is_authenticated:
        return redirect("login")

    subject = Subject.objects.get(id=subject_id)
    if request.method == "POST":
        subName = request.POST["subName"]
        numUnits = request.POST["numUnits"]
        subStart = request.POST["subStart"] or None
        subEnd = request.POST["subEnd"] or None
        reqName1, gradeNum1 = request.POST["reqName1"], request.POST["gradeNum1"]
        reqName2, gradeNum2 = request.POST["reqName2"], request.POST["gradeNum2"]
        reqName3, gradeNum3 = request.POST["reqName3"], request.POST["gradeNum3"]
        reqName4, gradeNum4 = request.POST["reqName4"], request.POST["gradeNum4"]
        reqName5, gradeNum5 = request.POST["reqName5"], request.POST["gradeNum5"]
        subjDays = request.POST.getlist("subjDays")

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
        subject.subjDays = subjDays

        subject.save()

    return redirect("editSub")

def help_view(request):
    return render(request, 'help.html')


def removeSubForm(request, subject_id):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":        
        subject = Subject.objects.get(id=subject_id)
        subject.delete()

    return redirect("editSub")