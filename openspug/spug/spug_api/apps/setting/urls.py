# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the MIT License.
# from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^ldap_test/$', ldap_test),
    url('', SettingView.as_view()),
]
