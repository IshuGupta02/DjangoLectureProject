from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.utils.timezone import now
from .models import TodoList
from .models import TodoItem
from django.views.generic import TemplateView
from .forms import InputForm_1
from datetime import datetime


def index(request):
    todolists = TodoList.objects.all()
    items = TodoItem.objects.all()
    template = loader.get_template('todo/index.html')
    context = {
        'todolists': todolists,
    }
    return render(request, 'todo/index.html', context)

def detail(request, list_id):
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    items_list = TodoItem.objects.filter(todo_list=todolist)
    form = InputForm_1()
    context = {
        'todolist': todolist,
        'items_list': items_list,
    }
    return render(request, 'todo/detail.html', context)

def create(request):
    if request.method == "GET":
        return render(request, 'todo/createlist.html')

    name = request.POST["name"]
    TodoList.objects.create(list_name=name)
    # lists = TodoList.objects.all()
    # context = {
    #     'todolists': lists,
    # }
    return redirect("../")

def add(request, list_id):
    
    todolist = TodoList.objects.get(id=list_id)
    items_list = TodoItem.objects.filter(todo_list=todolist)
    context = {
        'todolist': todolist,
        'items_list': items_list
    }

    if request.method == "POST":

        name = request.POST["name"]
        date = request.POST["duetime"]
        # print(date)
        TodoItem.objects.create(title=name,due_date=date,todo_list=todolist)

    return redirect("../"+str(list_id))

def delete_item(request, todolist_id, item_id):
    TodoItem.objects.filter(id=item_id).delete()
    try:
        todolist = TodoList.objects.get(id=todolist_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    # items_list = TodoItem.objects.filter(todo_list=todolist)
    # context = {
    #     'todolist': todolist,
    #     'items_list': items_list
    # }
    return redirect("../../"+str(todolist_id))

def update_item(request, todolist_id, item_id):
    
    todolist = TodoList.objects.get(id=todolist_id)
    item= TodoItem.objects.get(id=item_id)
    context = {
        'item': item
    }
    if request.method == "POST":
        name = request.POST["item"]
        date = request.POST["duetime"]
        item.title= name
        item.due_date= date
        
        checked_ = request.POST["checked"]
        if checked_=="on":
            item.checked=True
        else:
            item.checked=False
        
        item.save()
        return redirect("../../"+str(todolist_id))
    else:
        return render(request, 'todo/update.html', context)

def delete_list(request, todolist_id):
    TodoList.objects.filter(id=todolist_id).delete()

    # todolists = TodoList.objects.all()
    # # context = {
    # #     'todolists': todolists,
    # # }
    return redirect("../")

# def sample(request):
#     context ={}
#     context['form']= InputForm()
#     return render(request, "todo/sampleDateTime.html", context)
def sample(request):
    if request.method == "POST":
        form = InputForm_1(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error ", form.errors)
    form = InputForm_1()
    return render(request, 'todo/sampleDateTime.html', {'form':form})
