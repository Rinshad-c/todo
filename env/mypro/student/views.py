from django.shortcuts import redirect,render
from django.shortcuts import render
from . form import Todoforms
from . models import Todo
from django.http import HttpResponse

# Create your views here.
def home(request):
    form=Todoforms()
    todos=Todo.objects.all()
    context={
        'form':form,
        'todos':todos
    }
    if request.method=="POST":
        form=Todoforms(request.POST)
    if form.is_valid():
        form.save()  
        return render(request,"home.html",context) 



    return render(request,"home.html",context)

def delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=='POST':
        todo.delete()
        return redirect("home")

def edit(request,id):
    todos=Todo.objects.get(id=id)
    form=Todoforms(instance=todos)
    context={
        'form':form
    }
    if request.method=="POST":
        form=Todoforms(request.POST,instance=todos)
    if form.is_valid():
        form.save()    
        return redirect('home')

    return render(request,"edit.html",context)