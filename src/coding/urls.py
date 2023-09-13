#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : SQL_memOJi
* File Name    : urls.py
* Description  : 
* Create Time  : 2021-04-05 11:32:17
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
from . import apis

app_name = 'coding'
urlpatterns = [

    # Coding Page
    path('', views.coding, name='index'),
    path('coding-editor/<event_type>/<event_id>/<ques_id>/', views.CodingEditor.as_view(), name='coding-editor'),
    path('statistics/', views.statistics, name='statistics'),

    # Management Pages
    path('exams-manage/', views.exams_manage, name='exams-manage'),
    path('exams-manage/exam-add/', views.exam_add, name='exam-add'),
    path('exams-manage/exer-add/', views.exer_add, name='exer-add'),
    # path('exams-manage/exam-delete/', views.exam_delete, name='exam-delete'),
    # path('exams-manage/exer-delete/', views.exer_delete, name='exer-delete'),
    # path('exams-manage/exam-edit/<exam_id>/', views.exam_edit, name='exam-edit'),
    # path('exams-manage/exer-edit/<exer_id>/', views.exer_edit, name='exer-edit'),

    # Questions-Manage Page
    path('questions-manage-base/',      views.questions_manage_base, name='questions-manage-base'),
    path('questions-manage/',           views.questions_manage, name='questions-manage'),
    path('questions-manage/add/',       views.question_add, name='question-add'),
    path('questions-manage/delete/',    views.question_delete, name='question-delete'),
    path('questions-manage/edit/<question_id>/', views.question_edit, name='question-edit'),
    
    # Ques-set-manage Page
    path('ques-set-manage/',        views.ques_set_manage, name='ques-set-manage'),
    path('ques-set-manage/add/',    views.ques_set_add, name='ques-set-add'),
    path('ques-set-manage/delete/', views.ques_set_delete, name='ques-set-delete'),
    path('ques-set-manage/edit/<ques_set_id>/', views.ques_set_edit, name='ques-set-edit'),

    # Papers-manage Page
    path('papers-manage/',      views.papers_manage, name='papers-manage'),
    path('papers-manage/add/',  views.paper_add, name='paper-add'),
    # path('papers-manage/delete/', views.paper_delete, name='paper-delete'),
    # path('papers-manage/edit/<paper_id>/', views.paper_edit, name='paper-edit'),

    # # APIs
    # path('api/test/', apis.test_api, name='api-test'),
    # path('api/question-list/', apis.question_list, name='question-list'),

    # Analysis
    path('analysis/<event_type>/<event_id>/', views.PaperDetails.as_view(), name='analysis'),
    path('teacheranalysis/<event_type>/<event_id>/', views.ExamExerTeacherDetails.as_view(), name='teacher-analysis'),
]
