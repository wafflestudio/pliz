from django.conf.urls import url
from errands import views

urlpatterns = [
    url(r'^$', views.ErrandList.as_view(), name='errand_list' ),
    url(r'^(?P<pk>[0-9]+)/$', views.ErrandDetail.as_view() ),
    url(r'^delivery/$', views.Delivery.as_view() ),
    url(r'^homework/$', views.Homework.as_view() ),
    url(r'^etc/$', views.Etc.as_view() ),
]