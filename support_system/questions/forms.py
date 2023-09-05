from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Проблема'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание проблемы'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Решение проблемы'
            })

        }
