# Generated by Django 3.0.7 on 2020-06-13 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=254)),
                ('avatar', models.CharField(default='http://ahriknow.oss-cn-beijing.aliyuncs.com/avatar.jpg', max_length=254)),
                ('number', models.CharField(max_length=30, unique=True)),
                ('nickname', models.CharField(max_length=254, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=254, null=True)),
                ('sex', models.CharField(max_length=10, null=True)),
                ('age', models.SmallIntegerField(null=True)),
                ('birthday', models.DateTimeField(null=True)),
                ('image', models.CharField(max_length=254, null=True)),
                ('introduce', models.TextField(null=True)),
                ('info', models.TextField(null=True)),
                ('email', models.CharField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('qq', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
