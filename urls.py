from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoPlatforRestriction.views.home', name='home'),
    # url(r'^djangoPlatforRestriction/', include('djangoPlatforRestriction.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'example.views.home'),
    url(r'^not_allowed/', 'example.views.not_allowed_home'),
)
