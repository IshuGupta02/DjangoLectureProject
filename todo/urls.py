from django.urls import path

from .views import index, detail, create, add, update_item, delete_item, delete_list
from .views import sample



app_name='todo'
urlpatterns = [
    path('', index, name='index'),
    path('<int:list_id>/', detail, name='list_details'),
    path('create/', create, name='list_create'),
    path('<int:list_id>/add_item',add, name='add_item'),
    path('sample/', sample, name="sample"),
    path('update/<int:todolist_id>/<int:item_id>',update_item, name='update_item'),
    path('delete/<int:todolist_id>/<int:item_id>',delete_item, name='delete_item'),
    path('delete_list/<int:todolist_id>',delete_list, name='delete_list'),
    
]