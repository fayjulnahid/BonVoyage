from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.index, name='base_template'),

    url(r'^user_profile/$', views.UserProfile, name="user_profile"),
    url(r'^create_profile/$', views.createProfile, name="create_profile"),
    path('about/', views.about, name='about'),
]