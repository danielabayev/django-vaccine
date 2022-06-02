from django.urls import re_path as url
from django.urls import path
from VaccineApp import views

urlpatterns = [
    url(r'^Human$', views.human_api),
    url(r'^Human/([0-9+])$', views.human_api),
    path('Excel', views.save_file),
]
