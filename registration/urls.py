from django.contrib import admin
from django.urls import path
from .views import CourseView,StudentRegView


app_name= "registration"

urlpatterns = [
    path('', StudentRegView.as_view(),name="student_reg"),
    path('course/', CourseView.as_view(),name="course_reg"),
]
