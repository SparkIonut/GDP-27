from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Welcome/$', views.Welcome, name='welcome'),
    url(r'Ethics/$', views.Ethics, name='ethics'),
    url(r'Terms/$', views.Terms, name='terms'),
    url(r'Login/$', views.Login, name='login'),
]