from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cal', views.get_calendar_date, name = 'cal-index'),
]