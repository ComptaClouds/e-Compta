from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from ComptaCloud.views import login_redirect
from accounts.views import activate
from django.views.generic.base import TemplateView


urlpatterns = [
    #url('', include('django.contrib.auth.urls')),
    url(r'^$', login_redirect,name='login_redirect'),
    url('admin/', admin.site.urls),
    url('account/', include('accounts.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    #path(r"^account/signup/$", account.views.SignupView.as_view(), name="account_signup"),
    #path(r"^account/", include("account.urls")),
    #path('', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)