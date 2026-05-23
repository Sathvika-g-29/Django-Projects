from django.urls import path
from . import views

urlpatterns=[path('',views.home),path('colleges/',views.colleges),path('students/',views.students),path('address/',views.address),path('db/',views.db,name='db')]