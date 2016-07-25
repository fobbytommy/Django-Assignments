from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="products_index"),
    url(r'^show/(?P<id>\d+)$', views.show, name="products_show"),
    url(r'^edit/(?P<id>\d+)$', views.edit, name="products_edit"),
	url(r'^destroy/(?P<id>\d+)$', views.destroy, name="products_destroy"),
	url(r'^new$', views.new, name="products_new"),
]
