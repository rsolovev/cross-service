from django.conf.urls import url
from crossservice import views

# SET THE NAMESPACE!
app_name = 'crossservice'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
