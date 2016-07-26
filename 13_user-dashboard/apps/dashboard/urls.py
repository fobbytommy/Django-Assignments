from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register_page, name="register"),
    url(r'^process/(?P<process>\w+)$', views.process_user, name="process_user"),
	url(r'^home$', views.success, name="success"),
	url(r'^logout$', views.logout, name="logout"),
]
