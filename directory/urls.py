from django.conf.urls import *
import views
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ksa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^4/$', RedirectView.as_view(url='/')),
    url(r'^(?P<pk>[\d-]+)/$', views.ksa_view, name='ksa_view'),
    url(r'^update/4/$', RedirectView.as_view(url='/')),
    url(r'^update/(?P<pk>[\w-]+)/$', login_required(views.KSAUpdate.as_view(), login_url='/login/'), name='KSAUpdate'),
    url(r'^toupdate/$', views.toupdate, name='toupdate'),
)