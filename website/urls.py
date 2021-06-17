from django.urls import path
from website.views import getStart, json

urlpatterns = [
    path('start', getStart),
    path('Json', json)
]
