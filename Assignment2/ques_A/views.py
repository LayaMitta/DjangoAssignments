from django.shortcuts import render
import operator
from django.http import HttpResponse
def home(requests):
    return render(requests,'ques_A/home.html')
def calculate(requests):
    op=requests.GET['operator']
    num1=float(requests.GET['Integer1'])
    num2=float(requests.GET['Integer2'])
    if(op=='+'):
        ans=num1+num2
    elif(op=='-'):
        ans=num1-num2
    elif(op=='*'):
        ans=num1*num2
    else:
        ans=num1/num2
    return render(requests,'ques_A/calculate.html',{'Result':ans})
    

# Create your views here.
