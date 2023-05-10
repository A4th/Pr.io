from django.db import models

# Create your models here.


class Task(models.Model):
    reqType = models.CharField(max_length=50,default = "")

    taskName = models.CharField(max_length=50,default = "")
    dueDate = models.DateTimeField()
    def __str__(self):
        return self.taskName


class Subject(models.Model):
    # subID = models.IntegerField()
    subName = models.CharField(max_length=50)
    numUnits = models.IntegerField()
    subStart = models.DateTimeField()
    subEnd = models.DateTimeField()

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

    def __str__(self):
        return self.subName 