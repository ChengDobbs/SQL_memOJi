#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : SQL_memOJi
* File Name    : urls.py
* Description  :
* Create Time  : 2021-04-04 15:45:56
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh/SQL_memOJi
----------------------------------------------------------------------------------------------------
* Notice
-
-
----------------------------------------------------------------------------------------------------
'''

from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    # Global Pages
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('blank/', views.blank, name='blank'),
    path('e404/', views.e404, name='e404'),
    path('e500/', views.e500, name='e500'),

    # Auth Pages
    path('auth-base/', views.auth_base, name='auth-base'),
    path('auth-login/', views.AuthLogin.as_view(), name='auth-login'),
    path('auth-logout/', views.auth_logout, name='auth-logout'),
    path('auth-recoverpw/', views.auth_recoverpw, name='auth-recoverpw'),
    path('auth-register/', views.AuthRegister.as_view(), name='auth-register'),
    path('auth-register-done/', views.auth_register_done, name='auth-register-done'),
    path('auth-status/', views.auth_status, name='auth-status'),

    # User-management Pages
    path('user-manage/', views.UserDetails.as_view(), name='user-manage'),
    path('user-info/', views.UserDetails.as_view(), name='user-info'),

    # School-management Pages
    path('school-manage/', views.SchoolManage.as_view(), name='school-manage'),
    path('school-details/<school_id>/', views.SchoolDetails.as_view(), name='school-details'),


    # Class-management Pages
    path('class-manage/', views.ClassManage.as_view(), name='class-manage'),
    path('class-details/<class_id>/', views.ClassDetails.as_view(), name='class-details'),
    path('class-details/<class_id>/<event_type>/<event_id>', views.ClassEventDetails.as_view(), name='class-event'),
    
    # Student-management Pages
    path('student-manage/', views.StudentManage.as_view(), name='student-manage'),
    path('student-details/<student_id>/', views.StudentDetails.as_view(), name='student-details'),  



]
