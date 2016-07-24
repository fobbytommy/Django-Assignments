from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index, name="ran_index"),
	url(r'^generator$', views.generator, name="generator"),
	url(r'^reset$', views.reset, name="reset")
]
