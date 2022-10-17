from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class AddEmployeeAdmin(admin.ModelAdmin):
    list_display=['id','FirstName','LastName','gender']
    list_filter=['FirstName','LastName']
    search_fields=['id','FirstName',]

#admin.site.register(EmployeeForms)

admin.site.register(AddEmployee,AddEmployeeAdmin)
