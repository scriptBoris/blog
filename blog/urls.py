from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',                            views.post_list,     name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$',        views.post_detail,   name='post_detail'),
    url(r'^post/new/$',                   views.post_new,      name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',   views.post_edit,     name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete,   name='post_delete'),
    url(r'^page/(\d+)/$',                 views.post_list,     name='post_list'),
    url(r'^auth/login',                   views.login,         name='login'),
    url(r'^auth/logout',                  views.logout,        name='logout'),
    url(r'^auth/register',                views.register,      name='register'),
    url(r'^user/(?P<name>[a-z]+)$',       views.user,          name='user'),
]
