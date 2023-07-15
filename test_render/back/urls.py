from django.contrib import admin
from django.urls import path
from back.views import returnSimplePage

urlpatterns = [
    path('simple/', returnSimplePage,name="simple"),
]

