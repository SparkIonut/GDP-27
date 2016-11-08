from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Calendar/$', views.Calendar, name='calendar'),
]