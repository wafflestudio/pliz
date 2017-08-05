from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    url(r'^signup/$', views.user_signup, name='signup'),
    url(r'^api-token-auth/$', obtain_auth_token),
]