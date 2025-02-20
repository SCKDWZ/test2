from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def Index(request):
    return render(request,'index.html')
 
 
#博客列表   按分类显示  按照标签显示
def Blogslist(request):
    # 那get参数 拿type类型id
    type_id=request.GET.get('type')
    #拿标签参数
    tags_id=request.GET.get('tags')
    #根据参数获取属于当前类别的文章列表
    if type_id is None:
        # 如果没有分类  拿全部 判断标签id是否有值
        #拿到全部的文章数据
        if tags_id is None:
            blogs=Blogs.objects.all()
        else:
            #按标签拿数据
            t=Tags.objects.get(id=tags_id)
            blogs=Blogs.objects.filter(tags=t).order_by('-create_time')
    else:
        #按分类拿取文章数据
        blogs=Blogs.objects.filter(type_id=type_id)
    #分页
    paginator=Paginator(blogs,5)
    page=request.GET.get('page')
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    except EmptyPage:
        blogs=paginator.page(paginator.num_pages)
    #获取分类信息
    blogtypes=Type.objects.all()
    blogtags=Tags.objects.all()
    #组织数据
    data={
        'blogs':blogs,
        'blogtypes':blogtypes,
        'blogtags':blogtags
    }
    return render(request,'article.html',context=data)
#博客详情
def Bloginfo(request,pk):
    blog=Blogs.objects.get(id=pk)
    #阅读量+1
    blog.add_readnum()
    comments_list=blog.comments_set.all()
    return render(request,'detail.html',context={'blog':blog,'comments':comments_list})

#按标签查询文章
# def Tags_view(request,pk):
#     t=Tags.objects.get(id=pk)
#     blogs=Blogs.objects.filter(tags=t).order_by('-create_time')
#     return render(request,'article.html',context={'blogs':blogs})



#评论的视图函数
def AddComments(request,pk):
    #拿到被评论的博客
    blog=Blogs.objects.get(id=pk)
    blog.add_commentsnum()
    #评论的上一级
    acceptparent_id=request.POST.get('acceptparent')
    #拿到接受评论人
    targetuser_id=request.POST.get('targetuser')
    #拿到发送评论人
    senduser=request.user
    #拿到评论数据
    content=request.POST.get('content',"")
    # 思考在页面拿到这些数据 下一步怎么做
    # 构造保存数据
    data={
        'senduser':senduser,
        'content':content,
        'blog':blog
    }
    if targetuser_id is not None:
        data['acceptparent']=Comments.objects.get(id=acceptparent_id)
        data['targetuser']=User.objects.get(pk=targetuser_id)
    #保存评论数据
    Comments.objects.create(**data)
    return redirect(blog.get_detail_url())
