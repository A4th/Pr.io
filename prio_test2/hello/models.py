from django.db import models
import json
from django.conf import settings
from django.contrib.auth.models import User
# from .current_user import get_current_user

# Create your models here.
class DegreeProgram(models.Model):
    degName = models.CharField(max_length=255)
    jsonData = models.JSONField()
    def __str__(self):
        return self.degName


class Task(models.Model):
    subName = models.ForeignKey("Subject", on_delete=models.CASCADE)
    reqType = models.CharField(max_length=50,default = "")
    taskName = models.CharField(max_length=50,default = "")
    dueDate = models.DateTimeField()
    enrolee = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.taskName


class Subject(models.Model):
    # subID = models.IntegerField()
    subName = models.CharField(max_length=50)
    numUnits = models.IntegerField()
    subStart = models.DateTimeField(null=True)
    subEnd = models.DateTimeField(null=True)

    reqName1 = models.CharField(max_length=50,default = "")
    gradeNum1 = models.DecimalField(max_digits=5,decimal_places=2,default = 0)

    reqName2 = models.CharField(max_length=50,default = "")
    gradeNum2 = models.DecimalField(max_digits=5,decimal_places=2,default = 0)

    reqName3 = models.CharField(max_length=50,default = "")
    gradeNum3 = models.DecimalField(max_digits=5,decimal_places=2,default = 0)

    reqName4 = models.CharField(max_length=50,default = "")
    gradeNum4 = models.DecimalField(max_digits=5,decimal_places=2,default = 0)

    reqName5 = models.CharField(max_length=50,default = "")
    gradeNum5 = models.DecimalField(max_digits=5,decimal_places=2,default = 0)

    hello = User.objects.get(username='aforth').id
    enrolee = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=hello)

    def __str__(self):
        return self.subName 

    def save_model(self, request, obj, form, change):
        obj.enrolee = request.user.id
        super().save_model(request, obj, form, change)