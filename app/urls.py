from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    
    url(r'^accounts/login/$', auth_views.login, {'template_name' : 'login.html'}, name='login'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^accounts/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name = 'password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    
    url(r'^$', views.index, name='index'),
    
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^sales/(\d+)/$', views.sales_detail, name='sales_detail'),
    
    url(r'^join/$', views.join, name='join'),
    
    url(r'^producers/$', views.producers_list, name='producers'),
    
    url(r'^cart/$', views.cart, name='cart'),
    
    
    
]