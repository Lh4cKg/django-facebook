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

Setup
-----------------------------
* Add 'facebook' app in your Django project
* Add facebook app to INSTALLED_APPS in settings.py: ``'facebook'``
* Add project configuration in settings.py::

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
* Add this line to the urlpatterns in urls.py::
	
	urlpatterns = [
			url(r'^facebook/', include('facebook.urls',namespace='facebook')),
	]
* Create a migration and run server::
	
	$ python manage.py makemigrations
	$ python manage.py migrate
	$ python manage.py runserver

	# check it ``localhost:8000`` in your browser
* For registration and authentication, go to the following link::
	
	localhost:8000/facebook/facebook_login
	

Example
---------------------------------
To install the source ``facebook`` package from example project::
	
	create a virtual environment and activate it	
	$ virtualenv --python=python3 --no-site-packages myenv
	$ cd myenv && source bin/activate 
	cloning django-facebook
	$ git clone https://github.com/Lh4cKg/django-facebook.git
	$ cd example/dajngo_facebook
	installing requirements packages
	$ pip install -r requirements.txt

create a migration and run server::

	$ python manage.py migrate
	$ python manage.py runserver

check it ``localhost:8000`` in your browser
for registration and authentication, go to the following link ``localhost:8000/facebook/facebook_login``

Template Tags
-----------------------------------
To use the template tag to view the current user profile image, add the following line to a template::

	{% load picture %}
	{% if user.is_authenticated %}

		{% profile_picture user.facebook_id %} {# or {% profile_picture user.username %} #}

	{% endif %}

Source Code
-----------------

The source code can be found on github_.

Contributing
-----------------

There are plenty of ways to contribute to this project. If you think you’ve found a bug please submit an issue_.

License
------------------

``facebook`` package is distributed under MIT license_. 

.. _github: https://github.com/Lh4cKg/django-facebook/tree/master/facebook
.. _issue: https://github.com/Lh4cKg/django-facebook/issues
.. _license: https://github.com/Lh4cKg/django-facebook/blob/master/LICENSE