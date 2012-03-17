from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
# check in test
urlpatterns = patterns('',
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
