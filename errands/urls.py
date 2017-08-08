from django.conf.urls import url
from errands import views

urlpatterns = [
    url(r'^$', views.ErrandList.as_view() ),
    url(r'^(?P<pk>[0-9]+)/$', views.ErrandDetail.as_view() ),
    url(r'^DELIVERY/$', views.Delivery.as_view() ),
    url(r'^HOMEWORK/$', views.Homework.as_view() ),
    url(r'^ETC/$', views.Etc.as_view() ),
]