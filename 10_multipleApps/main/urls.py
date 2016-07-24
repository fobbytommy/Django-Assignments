"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.intro.urls')),
	url(r'^time-display/', include('apps.timedisplay.urls')),
	url(r'^disppearing-ninjas/', include('apps.ninjas.urls')),
	url(r'^random-word/', include('apps.randomWord.urls')),
	url(r'^courses/', include('apps.courses.urls')),
	url(r'^login-register/', include('apps.loginReg.urls'))
]
