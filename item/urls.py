from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from item import views



app_name = 'item'


urlpatterns = [
      path('home/', views.ItemView.as_view(), name='home'),
      path('summary/', login_required(TemplateView.as_view(template_name='summary_page.html')), name='summary'),
]