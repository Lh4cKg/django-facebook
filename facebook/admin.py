# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import FacebookProfile

@admin.register(FacebookProfile)
class FacebookProfileAdmin(admin.ModelAdmin):
	pass
		
