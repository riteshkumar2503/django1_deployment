from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app123'

urlpatterns = [
    url(r'^register/$', views.register_view, name='register_view_pattern_name'),
    url(r'^login/$', views.login_view, name='login_view_pattern_name'),

]