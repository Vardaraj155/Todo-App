from django.db import models
from django import forms
# Create your models here.
class Todo(models.Model):
    text=models.CharField(max_length=40)
    complete=models.BooleanField(default=False)

def __str__(self):
    return self.text

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
    widget=forms.TextInput( attrs={'id':'inpu', 'type':'text', 'name':'todojobs' }
    ))