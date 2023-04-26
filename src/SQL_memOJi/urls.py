#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : SQL_memOJi
* File Name    : urls.py
* Description  : 
* Create Time  : 2021-04-04 00:39:15
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh/SQL_memOJi
----------------------------------------------------------------------------------------------------
* Notice

SQL_memOJi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
----------------------------------------------------------------------------------------------------
'''


from django.contrib import admin
from django.urls import path, include
from django.views import static
from django.urls import path
import user.urls
import iCalendar.urls
import coding.urls
from user.views import e404, e500
from . import settings


urlpatterns = [
    # url('^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path('admin/', admin.site.urls),

    path('', include(user.urls)),
    path('calendar/', include(iCalendar.urls)),
    path('coding/', include(coding.urls)),
]

handler404 = e404
handler500 = e500
