from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
    password_change_done,
)

urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^registerProfile/$', views.registerProfile, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^account_activation_sent/$',views.account_activation_sent, name='account_activation_sent'),


    url(r'activate/(?P<uidb64>[0-9A-Za-z_\\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),


    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^password-change-done/$',password_change_done,name='password_change_done'),
    url(r'reset-password/$', password_reset,name='password_reset'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



