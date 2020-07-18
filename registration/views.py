from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CourseForm,Studentform
# Create your views here.


class CourseView(FormView):
    form_class      =   CourseForm
    template_name   =   'course_reg.html'
    success_url = reverse_lazy('registration:course_reg')

    def form_valid(self,form):
        submit=form.save()
        return super().form_valid(form)

class StudentRegView(FormView):
    form_class      =   Studentform
    template_name   =   'student_reg.html'
    success_url = reverse_lazy('registration:student_reg')

    def form_valid(self,form):
        submit=form.save()
        return super().form_valid(form)

