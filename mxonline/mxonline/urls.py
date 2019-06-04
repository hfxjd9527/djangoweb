"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
import xadmin
from users.views import LoginView, LogoutView, RegisterView, ActiveUserView, ForgetPwdView
from users.views import ResetView, ModifyPwdView, IndexView
from .settings import MEDIA_ROOT
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^captcha/', include('captcha.urls')),  # 配置验证码
    url(r'^ueditor/', include('DjangoUeditor.urls')),  # 配置富文本编辑器
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),  # 配置上传文件的的访问处理函数
    # debug修改为false后配置上传文件的的访问处理函数
    # url(r'^static/(?P<path>.*)/$', serve, {"document_root": STATIC_ROOT}),
    url(r'^org/', include('organization.urls', namespace='org')),  # 课程机构url配置
    url(r'^course/', include('courses.urls', namespace='course')),  # 课程相关url配置
    url(r'^users/', include('users.urls', namespace='users')),  # 课程相关url配置
]
# 全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error_500'
