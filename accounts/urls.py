from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='user_list'),
    url(r'^signup/$', views.user_signup, name='signup'),
    url(r'^login/$', obtain_auth_token),
    url(r'^myerrand/$', views.user_errand_list ),
    url(r'^profile/$', views.user_profile ),
    url(r'^update_introduction/$', views.update_user_introduction ),

]