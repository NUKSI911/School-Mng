from django import forms
from .models import Course_Registration,Student_Registration


class CourseForm(forms.ModelForm):
    class Meta:
        model   =   Course_Registration
        fields  =   '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_form(self):
        return self.request.user
    
    def save(self, commit=True):
        form = super(CourseForm, self).save(commit=False)
        if commit:
            form.save()
        return form

class Studentform(forms.ModelForm):
    class Meta:
        model   =   Student_Registration
        fields  =   '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_form(self):
        return self.request.user
    
    def save(self, commit=True):
        form = super(Studentform, self).save(commit=False)
        if commit:
            form.save()
        return form