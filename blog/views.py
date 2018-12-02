from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog, BlogType
from django.core.paginator import Paginator
# Create your views here.


def blog_list(request):    #讲所有的博客返回到模板页面


    blogs_all_list=Blog.objects.all()
    paginator=Paginator(blogs_all_list, 10) #每10篇进行分页
    page_num = request.GET.get('page', 1)  # 获取URL的页面参数（get请求）
    page_of_blogs=paginator.get_page(page_num) #对URL返回的值进行处理，获取页面


    context={}
    context['page_of_blogs']= page_of_blogs
    return render_to_response('blog_list.html',context)

def blog_detail(request, blog_pk):
    context={}
    context['blog']=get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog_detail.html',context)

def blogs_with_type(request, blog_type_pk):
    context={}
    blogs_type=get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs']=Blog.objects.filter(blog_type=blogs_type)
    context['blog_type']=blogs_type
    return  render_to_response('blogs_with_type.html',context)