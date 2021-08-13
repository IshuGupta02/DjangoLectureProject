"""
All models
"""
from django.db import models

class TodoList(models.Model):
    """
    List- eg IMG TODO LIST, acad TODO Item- what task it is
    """
    list_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.list_name}"

class TodoItem(models.Model):
    """
    Description of a Todo Item
    """
    title= models.CharField(max_length=100)
    checked= models.BooleanField(default= False)
    due_date= models.DateTimeField()

    todo_list = models.ForeignKey(to=TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.todo_list.list_name}: {self.title}"
