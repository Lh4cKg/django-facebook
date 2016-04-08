# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.conf import settings

# app imports
from .models import FacebookProfile
from .facebook import FacebookAuth

_Facebook = FacebookAuth(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)

def home(request):
	rc = RequestContext(request)
	message = "Fall in love Python and Linux"
	c = {}
	c['message'] = message
	return render_to_response('base.html',c,rc)

def callback(request):
	# import ipdb; ipdb.set_trace()
	if request.user.is_authenticated():
		return HttpResponseRedirect('/account/profile/')
	if not request.user.is_active:
		if request.GET.items():
			user_obj = None
			if 'facebook' in request.META['HTTP_REFERER']:
				code = request.GET['code']
				_Facebook._access_token(code)
				user_info = _Facebook._user_info()
				user_id = user_info['id']
				first_name = user_info.get('first_name')
				last_name = user_info.get('last_name')
				username = user_info.get('first_name') + user_info.get('last_name') #
				email = user_info.get('email')
				birthday = user_info.get('birthday')
				gender=user_info.get('gender')
				picture = user_info.get('picture')['data']['url']
				profile_url = '{u}{i}'.format(u=settings.FACEBOOK_URL,i=user_id)

				try:
					user_obj = User.objects.get(username=user_id)
				except User.DoesNotExist:
					user_obj = User.objects.create_user(
									username=user_id,
									email=email,
									first_name=first_name,
									last_name=last_name)

				try:
					profile = FacebookProfile.objects.get(user=user_obj.id)
					profile.access_token = _Facebook.access_token
				except FacebookProfile.DoesNotExist:
					profile = FacebookProfile(
								user=user_obj,
								facebook_id=user_id,
								first_name=first_name,
								last_name=last_name,
								birthday=birthday,
								email=email,
								gender=gender,
								picture=picture,
								profile_url=profile_url,
								access_token=_Facebook.access_token)
					profile.save()
			# else:
				# user_obj = User.objects.filter(username=user_id)

			user = authenticate(token=_Facebook.access_token, user=user_obj)
			login(request, user)
			return HttpResponseRedirect('/facebook/') #('/account/profile/')
	return HttpResponse('Welcome to Facebook')

def facebook_login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/account/profile/')
	facebook_url = _Facebook._authorize_url()
	return HttpResponseRedirect(facebook_url)