from dataclasses import fields
from.models import Task, Sem
from django.forms import ModelForm, widgets, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   "task": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
                   }

class SemForm(ModelForm):
    class Meta:
        model = Sem
        fields = ['content', "sem"]
        widgets = {"content": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   "sem": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   }
