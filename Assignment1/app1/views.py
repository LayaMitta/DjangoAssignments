from django.shortcuts import render
import operator
from django.http import HttpResponse
def home(requests):
    return render(requests,'app1/home.html',{'name':'Laya'})
    
def aboutme(requests):
    return render(requests,'app1/aboutme.html',{'userid':'Layauserid'})

def hobbies(requests):
    return render(requests,'app1/hobbies.html')
    

# Create your views here.
