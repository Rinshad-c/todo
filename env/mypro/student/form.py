from django import forms
from . models import Todo
from django.forms import TextInput

class Todoforms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
        widgets = {
            'title':TextInput(attrs={
                "type":"text",
                "class":"form-control",
                "placeholder":"enter a todo"

            })
        }