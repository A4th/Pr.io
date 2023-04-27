from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from .forms import Subjectform
from django.contrib import messages
from .models import Subject

# Create your views here.
def index(request):
    return HttpResponse("umabot ka")

def addSub(request):
    return render(request, 'add_subject.html')

def addTask(request):
    return render(request, "add_task.html")

def addCourseSub(request):
    return render(request, "add_course_subjects.html")

def viewSched(request):
    return render(request, "view_schedule.html")

def addSubForm(request):
    print("Hello World?????")
    # print(request)
    # print("Hello World????? 1", dir(request))
    # print(request.body)
    if request.method == "POST":
        print("TSENELIN")
        subName = request.POST["subName"]
        numUnits = request.POST["numUnits"]
        subStart = request.POST["subStart"]
        subEnd = request.POST["subEnd"]
        print(subName, numUnits, subStart, subEnd)
        addSub_details = Subject(subName = subName, numUnits = numUnits, subStart = subStart, subEnd = subEnd)
        addSub_details.save()
    
    print("KIMMY")
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


