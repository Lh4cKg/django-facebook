==================
 django-facebook
==================
Simple Django Facebook Authentication/Registration for Python 3, It uses the standard authentication build into Django.

Installation Requirements
--------------------------
* Python >= 3.0
* Django >= 1.7
* Requests 
* Simplejson

Setup:
--------

* Add 'facebook' app in your Django project.
* Add facebook app to INSTALLED_APPS in settings.py: `'facebook'`,
* Add project configuration in settings.py
	# Facebook configuration

	FACEBOOK_APP_ID = "" # your app id

	FACEBOOK_APP_SECRET = "" # your app secret

	FACEBOOK_URL = "http://www.facebook.com/"
	
	AUTHORIZE_URL = "https://graph.facebook.com/oauth/authorize"
	
	ACCESS_TOKEN_URL = "https://graph.facebook.com/oauth/access_token"
	
	API_URL = "https://graph.facebook.com/v2.5/"
	
	REQUEST_PERMISSIONS_URL = "https://www.facebook.com/dialog/oauth?"
	
	GRAPH_ME_URL = "https://graph.facebook.com/v2.5/me"
	
	FACEBOOK_SCOPE = ["email","user_birthday"] # publish_stream
	
	CALLBACK_URL = "http://localhost:8000/callback/"

	# Auth backends

	AUTHENTICATION_BACKENDS = (
	    'django.contrib.auth.backends.ModelBackend',

	    'facebook.backend.FacebookBackend',
	)
		
	

Example:
----------
To install the source ``facebook`` package::
	
	create a virtual environment and activate it	
	$ virtualenv --python=python3 --no-site-packages myenv
	$ cd myenv && source bin/activate 
	cloning django-facebook
	$ git clone https://github.com/Lh4cKg/django-facebook.git
	$ cd dajngo_facebook
	installing requirements packages
	$ pip install -r requirements.txt

Usage:
--------

	create a migration and run server
	$ python manage.py migrate
	$ python manage.py runserver

check it ``localhost:8000`` in your browser
for registration and authentication, go to the following link ``localhost:8000/facebook/facebook_login``



