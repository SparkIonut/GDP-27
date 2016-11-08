from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^User/(?P<account_id>\d+)$', views.Account, name='account'),
    url(r'^My_Account$', views.My_Account, name='my_account'),
    url(r'^logout$', views.Logout, name='logout'),
]