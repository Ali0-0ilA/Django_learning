from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse

def getStart(request):
    return render(request, 'index.html')

# def json(request):
#     return JsonResponse({'name':'ali'})