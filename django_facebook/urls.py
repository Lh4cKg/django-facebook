from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^facebook/', include('facebook.urls',namespace='facebook')),
	url(r'^', include('facebook.urls',namespace='facebook')),
	url(r'^admin/', include(admin.site.urls)),
]
