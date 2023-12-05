from django.urls import path
from user_auth import views

app_name = 'user_auth'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
]