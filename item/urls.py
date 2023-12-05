from django.urls import path
from item import views


app_name = 'item'


urlpatterns = [
      path('home/', views.ItemView.as_view(), name='home'),
]
