# -*- coding: utf-8 -*-
# @AuThor  : frank_lee
from django.conf.urls import url
from .views import CourseListView, CourseDetailView, CourseInfoView, CourseCommentsView, AddCommentsView
urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),  # 课程机构页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),  # 课程详情页
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),  # 课程章节页
    url(r'^comments/(?P<course_id>\d+)/$', CourseCommentsView.as_view(), name='course_comments'),  # 课程章节页
    url(r'^add_comments/$', AddCommentsView.as_view(), name='add_comments'),  # 添加课程评论
]
