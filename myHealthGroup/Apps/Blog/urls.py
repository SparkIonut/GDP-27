from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Blog$', views.Blog, name='blog'),
    url(r'^Post/(?P<post_id>\d+)/$', views.Post_Page, name='post'),
    url(r'^Post/(?P<post_id>\d+)/like$', views.Like_Post, name='like_post'),
    url(r'^Post/(?P<post_id>\d+)/dislike$', views.Dislike_Post, name='unlike_post'),
    
    url(r'^My_Post$', views.My_Posts, name='my_posts'),
    url(r'^Create_Post$', views.Create_Post, name='create_post'),
    url(r'^Post/(?P<post_id>\d+)/edit$', views.Edit_Post, name='edit_post'),
]