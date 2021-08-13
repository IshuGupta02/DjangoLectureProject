from django import forms
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminSplitDateTime
from .models import TodoItem
# creating a form 
# class InputForm(forms.Form):
#     title= forms.CharField(max_length=100)
#     checked= forms.BooleanField()
#     # date_input= forms.DateField(widget= AdminDateWidget())
#     # time_input= forms.DateField(widget= AdminTimeWidget())
#     date_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())

class InputForm_1(forms.ModelForm):
    # date_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Meta:
        model = TodoItem
        fields = ('title', 'checked', 'due_date')
        widgets = {
            'due_date': AdminSplitDateTime(),
        }
       
