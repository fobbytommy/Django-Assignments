from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='loginReg_index'),
	url(r'^process/(?P<which_process>\w+)$', views.process, name='loginReg_process'),
	url(r'^success$', views.success, name='loginReg_success')
]
