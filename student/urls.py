from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('students/',views.studentlist),
    path('students/<int:id>/',views.student_details),
]
