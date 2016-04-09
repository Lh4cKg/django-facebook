==================
# django-facebook
==================
Simple Django Facebook Authentication/Registration for Python 3, It uses the standard authentication build into Django.

Installation Requirements
-----------------------------------
* Python >= 3.0
* Django >= 1.7
* Requests 
* Simplejson

To install the source ``facebook`` package::
	
	create a virtual environment and activate it	
	$ virtualenv --python=python3 --no-site-packages myenv
	$ cd myenv && source bin/activate 
	cloning django-facebook
	$ git clone https://github.com/Lh4cKg/django-facebook.git
	$ cd dajngo_facebook
	installing requirements packages
	$ pip install -r requirements.txt

Usage::

	create a migration and run server
	$ python manage.py migrate
	$ python manage.py runserver
check it ``localhost:8000`` in your browser
for registration and authentication, go to the following link ``localhost:8000/facebook/facebook_login``

Setup::

