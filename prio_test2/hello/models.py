from django.db import models

# Create your models here.


class Task(models.Model):
    reqID = models.IntegerField()
    reqName = models.CharField(max_length=50)
    dueDate = models.DateTimeField()


class Subject(models.Model):
    # subID = models.IntegerField()
    subName = models.CharField(max_length=50)
    numUnits = models.IntegerField()
    subStart = models.DateTimeField()
    subEnd = models.DateTimeField()

    def __str__(self):
        return self.subName + '   ' +  str(self.numUnits) + '   ' + str(self.subStart.day) +'   '+ str(self.subEnd.day)