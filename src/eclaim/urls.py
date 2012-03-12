from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eclaim.views.home', name='home'),
    # url(r'^eclaim/', include('eclaim.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    #index page
    url(r'^eclaim/$', 'eclaim.views.index'),

    #authentication
    url(r'^eclaim/auth/',
        include('eclaim.auth.urls')),

    #human resource pages
    url(r'^eclaim/hr/',
        include('eclaim.humanresource.urls')
        ),

    #expense page
    url(r'^eclaim/expense/',
        include('eclaim.expense.urls')
        ),
)
