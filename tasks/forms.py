##############
#  新規作成  #
##############

from django import forms
from django.forms import ModelForm

from .models import *
import bootstrap_datepicker_plus as datetimepicker

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Add new content...'}))
    class Meta:
        model = Task
        fields = '__all__'
        #read_only_fields = ('created', 'updated')
        exclude = ('created', 'updated', )
        ### プルダウン形式
        '''
        widgets = {
            'duedate': forms.SelectDateWidget
        }
        '''
        ### カレンダー形式
        widgets = {
            'duedate': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                options={
                     'locale': 'ja',
                     'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }