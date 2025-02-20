from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
#继承AbstractUser类 实际上django用户的user也是继承他
# 现在我用自己的类代替django的

class UserInfo(AbstractUser):
    #添加自己的数据字段
    wechat=models.CharField(verbose_name='微信',blank=True,null=True,max_length=32,default='')
