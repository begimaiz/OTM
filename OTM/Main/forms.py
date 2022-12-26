from .models import Task
from django.forms import ModelForm, Textarea, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

        widget = {
            'title': TextInput(attrs={

                'placeholder': 'please enter title for a task',
                'class': 'form-control'
            }),

            'description': Textarea(attrs={

                'placeholder': 'please enter description',
                'class': 'form-control'
            })
        }


