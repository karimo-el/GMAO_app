from django.urls import path
from . import views

urlpatterns = [
    path('',views.handel_work_request, name = 'handel_work_request'),

] 