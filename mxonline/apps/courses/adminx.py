# -*- coding: utf-8 -*-
# @AuThor  : frank_lee
import xadmin
from .models import Course, Lesson, Video, CourseResource, BannerCourse


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CoursedAdmin(object):
    list_display = ['name', 'desc', 'detail',  'degree',  'learn_times',  'students', 'fav_nums', 'get_zjs_nums']
    search_fields = ['name', 'desc', 'detail',  'degree',  'learn_times',  'students', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'detail',  'degree',  'learn_times',  'students', 'fav_nums', 'click_nums', 'add_time']
    relfield_style = 'fk-ajax'
    inlines = [LessonInline, CourseResourceInline]
    style_fields = {"detail": 'ueditor'}

    def queryset(self):
        qs = super(CoursedAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        # obj实际是一个course对象
        obj = self.new_obj
        # 如果这里不保存，新增课程，统计的课程数会少一个
        obj.save()
        # 确定课程的课程机构存在。
        if obj.course_org is not None:
            #找到添加的课程的课程机构
            course_org = obj.course_org
            #课程机构的课程数量等于添加课程后的数量
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


class BannerCoursedAdmin(object):
    list_display = ['name', 'desc', 'detail',  'degree',  'learn_times',  'students', 'fav_nums', 'image',  'click_nums', 'add_time', 'get_zjs_nums']
    search_fields = ['name', 'desc', 'detail',  'degree',  'learn_times',  'students', 'fav_nums', 'image',  'click_nums']
    list_filter = ['name', 'desc', 'detail',  'degree',  'learn_times',  'students', 'fav_nums', 'image',  'click_nums', 'add_time']
    relfield_style = 'fk-ajax'
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCoursedAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessionAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']
    list_editable = ['name']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CoursedAdmin)
xadmin.site.register(BannerCourse, BannerCoursedAdmin)
xadmin.site.register(Lesson, LessionAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)




