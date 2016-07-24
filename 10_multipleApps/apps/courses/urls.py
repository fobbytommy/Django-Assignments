from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='course_index'),
	url(r'^courses/add$', views.add, name='course_add'),
	url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name='course_destroy'),
	url(r'^courses/comment/(?P<id>\d+)$', views.comment, name='course_comment'),
	url(r'^courses/add_user$', views.add_user, name='course_add_user')
]
