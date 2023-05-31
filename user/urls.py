from django.urls import path
from . import views
from .views import validate_username

urlpatterns = [
    path('', views.home, name='profile'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('validate_username', validate_username, name='validate_username')
]
