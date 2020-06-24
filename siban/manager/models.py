from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=254, unique=True)
    number = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=254)
    avatar = models.CharField(max_length=254, default='http://ahriknow.oss-cn-beijing.aliyuncs.com/avatar.jpg')
    nickname = models.CharField(max_length=254, null=True)
    update_time = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user'


class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    update_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=254, null=True)
    sex = models.CharField(max_length=10, null=True)
    age = models.SmallIntegerField(null=True)
    birthday = models.DateTimeField(null=True)
    image = models.CharField(max_length=254, null=True)
    introduce = models.TextField(null=True)
    info = models.TextField(null=True)
    email = models.CharField(max_length=254, null=True)
    phone = models.CharField(max_length=20, null=True)
    qq = models.CharField(max_length=20, null=True)

    user = models.ForeignKey('manager.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_info'

