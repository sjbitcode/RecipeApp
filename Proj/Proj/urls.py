from django.conf.urls import patterns, include, url
from django.contrib import admin
from myrecipe import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page':'/'}, name="logout"),
    url(r"", include("chef.urls", namespace = "chef")),
    url(r"", include('myrecipe.urls', namespace='myrecipe')),
)
