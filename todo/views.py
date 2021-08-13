"""
Contains all views
"""
from django.shortcuts import render, redirect
from django.http import Http404
from .models import TodoList
from .models import TodoItem
from .forms import InputForm_1

def index(request):
    """
    Redirects to the index page
    """
    todolists = TodoList.objects.all()
    context={
        'todolists':todolists,
    }
    return render(request,'todo/index.html', context)

def detail(request, list_id):
    """
    Shows details of all
    items of a list
    """
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist as does_not_exist:
        raise Http404 from does_not_exist
    items_list = TodoItem.objects.filter(todo_list=todolist)
    context = {
        'todolist': todolist,
        'items_list': items_list,
    }
    return render(request, 'todo/detail.html', context)

def create(request):
    """
    creates a new todo list
    """
    if request.method == "GET":
        return render(request, 'todo/createlist.html')

    name = request.POST["name"]
    TodoList.objects.create(list_name=name)
    return redirect("../")

def add(request, list_id):
    """
    creates a new todo item
    """
    todolist = TodoList.objects.get(id=list_id)

    if request.method == "POST":
        name = request.POST["name"]
        date = request.POST["duetime"]
        TodoItem.objects.create(title=name,due_date=date,todo_list=todolist)

    return redirect("../"+str(list_id))

def delete_item(request, todolist_id, item_id):
    """
    deletes a todo item
    """
    TodoItem.objects.filter(id=item_id).delete()
    return redirect("../../"+str(todolist_id))

def update_item(request, todolist_id, item_id):
    """
    updates a todo item
    """
    item= TodoItem.objects.get(id=item_id)
    context = {
        'item': item
    }
    if request.method == "POST":
        # print(request.getAttribute())
        name = request.POST["item"]
        date = request.POST["duetime"]
        item.title= name
        item.due_date= date
        checked_= request.POST.get("checked", None)
        if checked_ is None:
            item.checked=False
        else:
            item.checked=True
        item.save()
        return redirect("../../"+str(todolist_id))
    return render(request, 'todo/update.html', context)

def delete_list(request, todolist_id):
    """
    deletes a todo list
    """
    TodoList.objects.filter(id=todolist_id).delete()
    return redirect("../")

def sample(request):
    """
    sample view to check Modelform
    """
    if request.method == "POST":
        form = InputForm_1(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error ", form.errors)
    form = InputForm_1()
    return render(request, 'todo/sampleDateTime.html', {'form':form})
    