from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="one_to_one_index"),
    url(r'^process$', views.process, name="process_one_to_one"),

]
