from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'analytics.views.home', name='analytics_home'),
)
