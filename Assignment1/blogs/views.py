from django.shortcuts import render
from django.http import HttpResponse
import operator
def drinks(requests):
    return HttpResponse('Drink 3l water')
def foods(requests):
    return HttpResponse('Eat healthy')


# Create your views here.
