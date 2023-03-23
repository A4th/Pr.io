from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addSub/", views.addSub, name="addSub"),
    path("addTask/", views.addTask, name="addTask"),
    path("addCourseSub/", views.addCourseSub, name="addCourseSub"),
    path("viewSched/", views.viewSched, name="viewSched")
]

#https://cdn.jsdelivr.net/npm/fullcalendar@6.1.5/index.global.min.js