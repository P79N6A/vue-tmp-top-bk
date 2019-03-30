# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from home_application.user_manage import user_views
from home_application.user_manage import my_views
from home_application.examination import page_one

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^login_info$', 'login_info'),
    (r'^search_user$', user_views.search_user),
    (r'^create_user$', user_views.create_user),
    (r'^update_user$', user_views.update_user),
    (r'^delete_user$', user_views.delete_user),
    (r'^SearchUser$', my_views.SearchUser),
    (r'^CreateUser$', my_views.CreateUser),
    (r'^DeleteUser$', my_views.DeleteUser),
    (r'^EditUser$', my_views.EditUser),
)

bkpatterns = patterns(
    'home_application.views',
    (r'^api/test$', page_one.test),
    (r'^search_biz$', page_one.search_biz),
    (r'^search_host$', page_one.search_host),
    (r'^add_monitor$', page_one.add_monitor),
    (r'^search_info$', page_one.search_info),
    (r'^delete_monitor$', page_one.delete_monitor),
)

urlpatterns += bkpatterns
