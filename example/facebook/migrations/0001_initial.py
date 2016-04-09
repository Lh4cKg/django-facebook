# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('facebook_id', models.CharField(max_length=100, verbose_name='Facebook ID')),
                ('first_name', models.CharField(null=True, max_length=100, verbose_name='First Name', blank=True)),
                ('last_name', models.CharField(null=True, max_length=100, verbose_name='Last Name', blank=True)),
                ('profile_url', models.CharField(null=True, max_length=50, verbose_name='Profile URL', blank=True)),
                ('email', models.EmailField(null=True, max_length=254, verbose_name='Email', blank=True)),
                ('birthday', models.CharField(null=True, max_length=100, verbose_name='Birthday', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', blank=True, default='M', null=True, choices=[('F', 'Female'), ('M', 'Male')])),
                ('picture', models.CharField(null=True, max_length=500, verbose_name='Picture', blank=True)),
                ('access_token', models.CharField(max_length=500, verbose_name='Access Token')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name_plural': 'Facebook Profiles',
                'verbose_name': 'Facebook Profile',
                'db_table': 'facebook_profiles',
            },
        ),
        migrations.AlterUniqueTogether(
            name='facebookprofile',
            unique_together=set([('user', 'facebook_id')]),
        ),
    ]
