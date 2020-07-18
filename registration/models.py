from django.db import models

# Create your models here.
class Course_Registration(models.Model):

    # user                 =   models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    course_name          =   models.CharField(max_length=60,null=False)
    course_code          =   models.CharField(max_length=10,null=False)
    category             =   models.CharField(max_length=30,null=False)
    start_date           =   models.DateField()
    end_date             =   models.DateField(auto_now=False, auto_now_add=False)
    participants         =   models.CharField(max_length=20)
    course_summary       =   models.CharField(max_length=250)
    course_type          =   models.CharField(max_length=25)
    maximum_participant  =   models.CharField(max_length=5)   


class Student_Registration(models.Model):
    
    first_name      =   models.CharField( max_length=50)
    last_name       =   models.CharField(max_length=50)
    Date_of_Birth   =   models.DateField( auto_now=False, auto_now_add=False)
    Blood_Group     =   models.CharField(max_length=2)
    Nationality     =   models.CharField(max_length=15)
    Email           =   models.EmailField(max_length=254)
    Religion        =   models.CharField(max_length=25)
    Phone_No        =   models.CharField(max_length=12)