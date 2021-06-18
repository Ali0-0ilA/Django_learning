from django.urls import path
from website.views import getStart

urlpatterns = [
    path('start', getStart),
    # path('Json', json)
]
