from django.conf.urls import url
from django.urls import path

from crossservice import views

# SET THE NAMESPACE!
app_name = 'crossservice'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^delete_account/$', views.user_delete, name='user_delete'),
    url(r'^update_account/$', views.user_update, name='user_update'),
    url(r'^post_service/$', views.post_service, name='post'),
    url(r'^delete_post/$', views.remove_service_post, name='post_delete'),
    url(r'^update_post/$', views.update_service_post, name='post_update'),
    path('posts/', views.listPosts.as_view(), name='posts'),
]
