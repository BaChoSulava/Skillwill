from django.shortcuts import render
import datetime

# Create your views here.

def get_calendar_date(request):
    now = datetime.datetime.now()
    return f"{now.year}/{now.month}/{now.day}"


