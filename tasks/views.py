################
##   ↓追加　###
################
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import *
import datetime
from django.core.mail import send_mail
from todo import settings

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    today = timezone.now().date()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form, "today":today}
    

    ##  メール送信機能
    '''
    time = datetime.datetime.now()
    time_str = time.strftime('%Y-%m-%d %H:%M')
    #time = datetime.datetime.strptime(nowtime,'%Y-%m-%d %H:%M')
    ##tasks = Task.objects.all()
    for task in tasks:
        if time >= (task.duedate - datetime.timedelta(days=1)):
    '''


    subject = 'タイトル：{}'.format("忘れてない・・・？")#(task.title)
    from_mail = settings.DEFAULT_EROM_EMAIL#['deeplearning408@gmail.com']
    recipient = ['deeplearning408@gmail.com']

    messages=""
    flag = False
    for task in tasks:
        if task.is_delay():
            messages = messages + 'タイトル：{}\n期日：{}\n\n'.format(task.title, task.duedate)
            flag = True
    if flag:
        print("忘れているタスクあり！メールを送信しました！")
        send_mail(subject, messages, from_mail, recipient)
    else:
        print("忘れているタスクはないよ！")

    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request, 'tasks/delete.html', context)

#######################
##  新規作成ページ   ##
#######################
def newTask(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'tasks/new_task.html', context)

'''
def sendMail():
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    time = datetime.datetime.strptime(nowtime,'%Y-%m-%d %H:%M')
    tasks = Task.objects.all()
    for task in tasks:
        if time >= (task.duedate - datetime.timedelta(days=1)):
            subject = 'タイトル：{}'.format(task.title)
            messages = 'メモ：{}\n期日：{}\n'.format(task.content, task.duedate)
            from_mail = []
            recipient = ['kotaxtech@gmail.com']
            send_mail(subject, message, from_mail, recipient)
'''