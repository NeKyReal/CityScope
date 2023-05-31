from django import forms
from django.forms import TextInput, EmailInput

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    widgets = {
        'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше имя'
        }),
        'email': EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }),
        'message': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш отзыв'
        })
    }


# class CreateForm(forms.Form):
#     name = forms.CharField(label="Название", widget=forms.TextInput(attrs={"placeholder": "Название мероприятия"}))
#     enter = forms.ChoiceField(label="Вход", choices=((1, "Свободный"), (2, "Платный"), (3, "По приглашению")))
#     capacity = forms.IntegerField(label="Вместимость", min_value=1, max_value=10)
#     photo = forms.ImageField(label="Фотография")
