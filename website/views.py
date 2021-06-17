from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def getStart(request):
    return HttpResponse('<h1>Hello World! </h1>')

def json(request):
    return JsonResponse({'name':'ali'})