from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addSub/", views.addSub, name="addSub"),
    path("addTask/", views.addTask, name="addTask"),
    path("addTask/<int:subject_id>",views.task_details,name = "task_details"),
    path("addCourseSub/", views.addCourseSub, name="addCourseSub"),
    path("viewSched/", views.viewSched, name="viewSched"),
    path("addSubForm/", views.addSubForm, name="addSubForm"),
    path("editSub/",views.edit_subject,name = "editSub"),
    path("editSub/<int:subject_id>",views.subject_details,name = "subject_details"),
    path("addTaskForm/", views.addTaskForm, name="addTaskForm"),

    path("checkSub/", views.checkSub, name="checkSub"),
    
]

#https://cdn.jsdelivr.net/npm/fullcalendar@6.1.5/index.global.min.js 