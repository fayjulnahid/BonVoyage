from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'events'

urlpatterns = [
    url(r'^all_events/$', views.hi, name="Events"),
    #url(r'^Enroll/', views.login_view, name="Enroll"),
]
