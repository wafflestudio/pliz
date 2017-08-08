from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='user_list'),
    url(r'^signup/$', views.user_signup, name='signup'),
    url(r'^login/$', obtain_auth_token),
    url(r'^myErrand/$', views.user_Errand_List ),
    url(r'^profile/$', views.user_Profile ),
]