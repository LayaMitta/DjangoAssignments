from django.shortcuts import render
from django.http import HttpResponse
import operator
def friends(requests):
    return HttpResponse('My friends contact list')
def family(requests):
    return HttpResponse('My family contact list')

# Create your views here.
