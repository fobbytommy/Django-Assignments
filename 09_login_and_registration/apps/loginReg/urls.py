from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
	url(r'^process/(?P<which_process>\w+)$', views.process),
	url(r'^success$', views.success)
]
