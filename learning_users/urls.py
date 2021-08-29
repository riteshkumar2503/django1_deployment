"""learning_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'special/', views.special_view_with_login_required, name='special_view_pattern_name'),
    url(r'^$', views.index_view,name='index_view_pattern_name'),
    url(r'^basic_app/', include('basic_app.urls')),  # here we are using INCLUDE to say that if anything begins with basic_app, for the rest of the url string search inside the urls.py file of basic_app
    url(r'^logout/$', views.logout_view, name='logout_view_pattern_name'),

]

