from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Article


# Create your views here.
class IndexView(generic.ListView):
    """
        首页视图,继承自ListVIew，用于展示从数据库中获取的文章列表
    """
    # 获取数据库中的文章列表
    model = Article
    # template_name属性用于指定哪个页面需要被渲染
    template_name = 'index.html'

