from email.policy import default
from tkinter.tix import Tree
from django.db import models

# Create your models here.
class AddEmployee(models.Model):
    Gender=(('male','male'),
            ('Female','Female'),
            ('Others','Others'))
    Married=(('Married','Married'),
    ('Unmarried','Unmarried')
    )
    FirstName=models.CharField(max_length=50)
    MiddleName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    gender=models.CharField(max_length=10,choices=Gender)
    DOB=models.DateField()
    Mobile=models.CharField(max_length=10)
    AlterMobile=models.CharField(max_length=10)
    Email=models.EmailField()
    Maritual_status=models.CharField(max_length=10,choices=Married)
    Blood=models.CharField(max_length=10)


def __str__(self):
    return self.FirstName
