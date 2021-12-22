from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

###############
##  ↓追加   ##
###############
class Task(models.Model):
    title = models.CharField(max_length = 200)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
        )
    print("created:{}".format(created))
    ## 更新日時の項目を追加
    updated = models.DateTimeField(
        auto_now = True
        )
    print("updated:{}".format(updated))
    ## 内容の項目を追加
    content = models.TextField(
        blank = True,
        null = True,
        max_length = 500
        )
    ## 期限日の項目を追加
    duedate = models.DateTimeField(
        default=timezone.now,
        blank = True
        )
    ## 時間を変数に代入
    
    def is_delay(self):
        duedate = self.duedate.date()
        return duedate == duedate.today()

    
    # strやprintを適用すると、__str__メソッドが呼び出される。
    # x = Task()
    # str(x)
    # print(x)
    def __str__(self):
        return self.title