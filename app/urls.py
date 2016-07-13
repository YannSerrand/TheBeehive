from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^sales/$', views.sales, name='index'),
    url(r'^sales/(\d+)/$', views.sales_detail, name='index'),
]