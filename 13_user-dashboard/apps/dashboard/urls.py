from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register_page, name="register"),
    url(r'^process/(?P<process>\w+)$', views.process_user, name="process_user"),
	url(r'^home$', views.success, name="success"),
	url(r'^logout$', views.logout, name="logout"),
	url(r'^manage/(?P<user_level>\w+)$', views.manage_users, name="manage_users"),
	url(r'^users/new$', views.new_user, name="new_user"),
	url(r'^users/delete/(?P<user_id>\d+)$', views.delete_user, name="delete_user"),
	url(r'^users/edit$', views.profile_edit, name="profile_edit"),
	url(r'^users/edit/(?P<user_id>\d+)$', views.edit_user_by_admin, name="edit_user_by_admin"),
	url(r'^users/show/(?P<user_id>\d+)$', views.user_wall, name="user_wall"),
	url(r'^add/message/(?P<to_who>\d+)$', views.add_message, name="add_message"),
	url(r'^add/post/(?P<message_id>\d+)/(?P<user_id>\d+)$', views.add_post, name="add_post")

]
