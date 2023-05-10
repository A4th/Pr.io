from django import forms
from .models import Subject,Task

class Subjectform(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subName', 'numUnits','subStart','subEnd','reqName1','gradeNum1'
                  ,'reqName2','gradeNum2',
                  'reqName3','gradeNum3',
                  'reqName4','gradeNum4',
                  'reqName5','gradeNum5'] 


class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['reqType','taskName','dueDate']
