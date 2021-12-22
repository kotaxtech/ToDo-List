##################
## ↓ 新規作成  ##
##################
from django.urls import path
from . import views

####################
##  bootstrap導入 ##
####################
from django_filters.views import FilterView
from django.urls import path, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from tasks.forms import TaskForm
#from tasks.filters import MyModelFilter
from tasks.models import Task

urlpatterns = [
    path('', views.index, name='list'),
    ## 新規作成ページ
    path('new_task/', views.newTask, name='new_task'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]
