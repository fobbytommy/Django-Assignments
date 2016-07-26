from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process_user/(?P<process>\w+)$', views.process_user, name="process_user"),
    url(r'^books/$', views.show_books, name="show_books"),
	url(r'^books/(?P<book_id>\d+)$', views.show_review, name="show_review"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^books/add$', views.add_books, name="add_books"),
    url(r'^books/add/review/(?P<book_id>\d+)/(?P<user_id>\d+)$', views.add_review, name="add_review"),
    url(r'^books/delete/review/(?P<book_id>\d+)/(?P<review_id>\d+)$', views.delete_review, name="delete_review"),
	url(r'^users/(?P<user_id>\d+)$', views.get_user, name="get_user")
]
