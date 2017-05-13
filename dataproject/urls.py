from django.conf.urls import patterns, include, url
from django.contrib import admin,auth
import settings
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'dataproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^traffic/', include('traffic.urls', namespace = 'traffic')),

    # url(r'^transit/', 'traffic.views.index2', name='index2'),
    # # Authentication
    # url(r'^login/$', auth.views.login),
    # url(r'^logout/$', auth.views.logout),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
