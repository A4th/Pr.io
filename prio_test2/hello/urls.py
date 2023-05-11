from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addSub/", views.addSub, name="addSub"),
    path("addTask/", views.addTask, name="addTask"),
    path("addTaskDetails",views.task_details,name = "task_details"),
    path("addTaskForm/", views.addTaskForm, name="addTaskForm"),
    path("addCourseSub/", views.addCourseSub, name="addCourseSub"),
    path("addCourseSubList/", views.addCourseSubList, name="addCourseSubList"),
    path("addCourseSubForm/", views.addCourseSubForm, name="addCourseSubForm"),
    path("viewSched/", views.viewSched, name="viewSched"),
    path("addSubForm/", views.addSubForm, name="addSubForm"),
    path("editSub/",views.edit_subject,name = "editSub"),
    path("editSubDetails/",views.subject_details,name = "subject_details"),
    re_path("editSub/(?P<subject_id>-?[0-9]+)/change\Z", views.editSubForm, name="editSubForm"),
    path("checkSub/", views.checkSub, name="checkSub"),

    #insert path here on add_course_subject
    
]

#https://cdn.jsdelivr.net/npm/fullcalendar@6.1.5/index.global.min.js
