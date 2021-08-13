from django.db import models
from django.utils.timezone import now

# Create your models here.

"""
List- eg IMG TODO LIST, acad TODO Item- what task it is

"""

class TodoList(models.Model):
    list_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.list_name}"

class TodoItem(models.Model):
    # id =models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title= models.CharField(max_length=100)
    checked= models.BooleanField(default= False)
    due_date= models.DateTimeField()

    todo_list = models.ForeignKey(to=TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.todo_list.list_name}: {self.title}"