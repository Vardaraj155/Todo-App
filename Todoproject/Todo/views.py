from django.shortcuts import render, redirect
from .models import Todo , TodoForm
# Create your views here.
def index(request):
    Todo_list=Todo.objects.order_by('id')
    form = TodoForm
    context={'Todo_list': Todo_list, 'form': form}
    return render(request, './index.html',context)

def addTodo(request):
    form=TodoForm(request.POST)
    if form.is_valid():
        newTodo=Todo(text=request.POST['text'])
        newTodo.save()    
    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete=True
    todo.save()
    return redirect('index')

def deletecompleted(request):
    compdel = Todo.objects.filter(complete__exact=True)
    compdel.delete()
    return redirect('index')    
    
def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')
