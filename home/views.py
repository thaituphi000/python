from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines("<H1>Xin chào</H1>")
    response.writelines("<H1>Đây là app Home</H1>")
    return response

