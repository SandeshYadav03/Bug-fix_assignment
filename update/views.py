from django.shortcuts import redirect,render
from .models import *
from .forms import *



def Main(request):
    obj=AddEmployee.objects.all()
    return render(request,'view.html',{'obj':obj})


def Uploadform(request):
    form=EmployeeForms()
    if request.method =='POST':
        form=EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "form.html",{"form":form})


def Detailed_View(request,id):
    emp=AddEmployee.objects.get(id=id)
    return render(request,'detailed_view.html',{'emp':emp})