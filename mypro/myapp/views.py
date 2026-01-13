from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')

def edit(request, EmpId):
    return render(request, 'edit.html')

def delete(request, EmpId):
   return render(request, 'delete.html')

def pagenotfound(request):
    return render(request, 'pagenotfound.html')