# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import (login,
                                       logout,
                                       password_change,
                                       password_change_done,
                                       password_reset,
                                       password_reset_done,
                                       password_reset_confirm
                                       )

urlpatterns = patterns('',
                       # login view
                       url(r'^login/$',
                           login,
                           {'template_name': 'auth/login.html',
                            'extra_context':
                                {
                                    'next': '/eclaim/index.html',
                                }
                            }),

                       # logout view
                       url(r'^logout/$',
                           logout,
                           {'next_page': '../login',
                            'template_name': 'auth/logout.html'
                            }),
                       
                       # password_reset
                       url(r'^password_reset/$',
                           password_reset,
                           {
                            'template_name': 'auth/password_reset.html',
                            'email_template_name':'auth/password_reset_email.html'
                            }),
                       # password_reset_done
                       url(r'^password_reset_done/$',
                           password_reset_done,
                           {
                            'template_name': 'auth/password_reset_done.html',
                            }
                           ),

                       # password_reset_confirm
                       url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>.+)/$',
                           password_reset_confirm,
                           {
                            'template_name': 'auth/password_reset_confirm.html',
                            'post_reset_redirect': '../logout' 
                            }),

                       # password change view
                       url(r'^password_change/$',
                           password_change,
                           {'template_name': 'auth/password_change.html',
                            'post_change_redirect': '../password_change_done'
                            }),

                       # password change done view
                       url(r'^password_change_done/$',
                           password_change_done,
                           {'template_name': 'auth/password_change_done.html'
                            }),
                       )