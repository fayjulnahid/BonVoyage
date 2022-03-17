from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    url(r'^$', views.all_events, name="Events"),
    url(r'^(?P<slug>[\w-]+)/$', views.event_detail, name="Event_details"),
    # url(r'^Enroll/', views.login_view, name="Enroll"),
]
