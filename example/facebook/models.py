# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class FacebookProfile(models.Model):
	user = models.ForeignKey(User,verbose_name=_('Username'))
	facebook_id = models.CharField(_('Facebook ID'),max_length=100)
	first_name = models.CharField(_('First Name'),max_length=100,blank=True,null=True)
	last_name = models.CharField(_('Last Name'),max_length=100,blank=True,null=True)
	profile_url = models.CharField(_('Profile URL'),max_length=50,blank=True,null=True)
	email = models.EmailField(_('Email'),blank=True,null=True)
	birthday = models.CharField(_('Birthday'),max_length=100,blank=True,null=True)
	M = 'M'
	F = 'F'
	VALUE = (
		(F, 'Female'),
		(M, 'Male'),
	)
	gender = models.CharField(_('Gender'),choices=VALUE,default=M,blank=True,null=True,max_length=1)
	picture = models.CharField(_('Picture'),max_length=500,blank=True,null=True)
	access_token = models.CharField(_('Access Token'),max_length=500)
	created = models.DateTimeField(_('Date'),auto_now_add=True)

	class Meta:
		app_label = 'facebook'
		db_table = 'facebook_profiles'
		ordering = ['created']
		unique_together = (('user', 'facebook_id'),)
		verbose_name = _('Facebook Profile')
		verbose_name_plural = _('Facebook Profiles')

	def __str__(self):
		return str(self.user)