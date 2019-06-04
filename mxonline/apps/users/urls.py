# -*- coding: utf-8 -*-
# @AuThor  : frank_lee
from django.conf.urls import url
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
from .views import MyCoursesView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),  # 修改用户头像
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),  # 用户个人中心修改密码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),  # 用户个人中心修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),  # 用户个人中心修改邮箱
    url(r'^mycourses/$', MyCoursesView.as_view(), name='mycourses'),  # 用户个人中心我的课程
    url(r'^mymessages/$', MyMessageView.as_view(), name='mymessages'),  # 用户个人中心我的消息
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name='myfav_org'),  # 用户个人中心我的收藏--课程机构
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name='myfav_teacher'),  # 用户个人中心我的收藏--授课教师
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name='myfav_course'),  # 用户个人中心我的收藏--公开课程
]
