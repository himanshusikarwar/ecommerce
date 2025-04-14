from django.http import HttpResponse


from asgiref.typing import HTTPRequestEvent
from django.shortcuts import render

# Create your views here.
def hello(request):
    print(request)
    return HttpResponse("hello world")