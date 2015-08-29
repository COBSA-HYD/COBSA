# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import COBSA.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', blank=True, max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('username', models.CharField(verbose_name='Username', unique=True, db_index=True, max_length=100)),
                ('email', models.EmailField(verbose_name='email address', max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('joined', models.DateTimeField(null=True, auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', COBSA.models.MyUserManager()),
            ],
        ),
    ]
