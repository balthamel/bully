from django.conf.urls import patterns, include, url
from HelloWorldApp import views


from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^HelloWorldApp/', include('HelloWorldApp.urls')),
	url(r'^HelloWorldApp/home/$', views.home,name='home'),
	url(r'^HelloWorldApp/form/$',views.form,name='form'),
	url(r'^HelloWorldApp/form/output/$',views.return_data,name='return_data'),
    
)

