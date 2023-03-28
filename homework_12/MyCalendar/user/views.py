from django.shortcuts import render
import datetime

# Create your views here.

def name(name, surname, born):
    now = datetime.datetime.now()
    number_of_years = now.year - born
    return f"{name}, {surname}, {number_of_years}"
