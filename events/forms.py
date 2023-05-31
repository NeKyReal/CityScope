from .models import Events, Review
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'announcement', 'description', 'date', 'place', 'image']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название события'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата проведения'
            }),
            'announcement': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс события'
            }),
            'place': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Примерное местоположение'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание события'
            })
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment']

        widgets = {
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            })
        }
