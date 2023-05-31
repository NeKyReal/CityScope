from django.urls import path
from .views import contact_form, home

urlpatterns = [
    path('', home, name='home'),
    path('contact-form/', contact_form, name='contact_form')
]
