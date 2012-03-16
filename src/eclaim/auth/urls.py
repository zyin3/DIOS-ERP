# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import (login,
                                       logout,
                                       password_change,
                                       password_change_done
                                       )

urlpatterns = patterns('',
                       # login view
                       url(r'^login/$',
                           login,
                           {'template_name': 'auth/login.html',
                            'extra_context':
                                {
                                    'next': '/eclaim/expense/new_expense/',
                                }
                            }),

                       # logout view
                       url(r'^logout/$',
                           logout,
                           {'next_page': '../login',
                            'template_name': 'auth/logout.html'
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
