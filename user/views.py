from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, UserLoginForm
from .json import json_reader


def home(request):
    list = json_reader("wishlist.json")
    wished_list = []
    for user in list:
        if user['user'] == request.user.id:
            wished_list.append(user['wish'])
    return render(request, 'user/profile.html', {'wishlist': wished_list})


class RegisterFormView(FormView):
    form_class = UserRegistrationForm
    success_url = "/user/login/"
    template_name = "user/register.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        return valid


def validate_username(request):
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)


class LoginFormView(FormView):
    form_class = UserLoginForm
    template_name = "user/login.html"
    success_url = "/events/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('all')
