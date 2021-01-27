from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import ToDoForm
# Create your views here.
def home(request):
    form = ToDoForm()
    todo_list = Todo.objects.order_by('id')
    context={'todo_list':todo_list,
                'form':form}
    return render(request,'mytodo/index.html',context)

@require_POST
def addToDo(request):
    form=ToDoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(task=request.POST['task'])
        new_todo.save()
    return redirect('home')

def completeToDo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completion_status = "done"
    todo.save()
    return redirect('home')

def changeToDoing(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completion_status = "doing"
    todo.save()
    return redirect('home')

def deleteCompleted(request):
    completed = Todo.objects.filter(completion_status__exact="done")
    completed.delete()
    return redirect('home')

def deleteAll(request):
    all_objects = Todo.objects.all()
    all_objects.delete()
    return redirect('home')

