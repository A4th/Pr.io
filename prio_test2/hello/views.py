from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

def addSub(request):
    return render(request, "add_subject.html")

def addTask(request):
    return render(request, "add_task.html")

def addCourseSub(request):
    return render(request, "add_course_subjects.html")

def viewSched(request):
    return render(request, "view_schedule.html")
