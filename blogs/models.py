from django.db import models
from django.urls import reverse
# Create your models here.
#创建博客相关的模型
#博客的分类  博客的标签  博客文章  博客评论

#博客的分类
class Type(models.Model):
    name=models.CharField(max_length=20,verbose_name='分类名称')
    describe=models.CharField(max_length=255,verbose_name='分类说明')
    def __str__(self):
        return  self.name
    # 获取对应分类id   构造路由  构造get请求参数
    def get_type_blogs_url(self):
        return reverse('blogs:blogslist')+'?type='+str(self.pk)
    class Meta:
        verbose_name='分类信息'
        verbose_name_plural=verbose_name
#博客的标签
class Tags(models.Model):
    name=models.CharField(max_length=20,verbose_name='标签名称')
    describe=models.CharField(max_length=255,verbose_name='标签说明')
    def __str__(self):
        return  self.name
    #获取标签id 构造路由 定义get传参
    def get_tag_blogs_url(self):
        return reverse('blogs:blogslist')+'?tags='+str(self.pk)
    class Meta:
        verbose_name='标签信息'
        verbose_name_plural=verbose_name

                          # 练习:   按数据需求  完成博客文章模型及评论模型
                           #    并将模型添加后台管理
from django.contrib.auth import get_user_model
User=get_user_model()
from django.utils.html import format_html
class Blogs(models.Model):
    blogstatus=(
        (1,'开放'),
        (2,'冻结')
    )
    title=models.CharField(max_length=255,verbose_name='标题')
    abstract=models.CharField(max_length=255,verbose_name='摘要')
    content=models.TextField(verbose_name='内容')
    top=models.BooleanField(default=False,verbose_name='是否置顶')
    img=models.ImageField(upload_to='blogs/imgs',verbose_name='封页图')
    readnum=models.IntegerField(default=0,verbose_name='阅读量')
    comment_num=models.IntegerField(default=0,verbose_name='评论量')
    status=models.IntegerField(choices=blogstatus,default=1,verbose_name='状态')
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time=models.DateTimeField(auto_now=True,verbose_name='最后修改时间')
    # 创建外键字段  关联用户，文章类型 文章标签
    #一对多 ForeignKey   一对一 OneToOneField 多对多 ManyToManyField
    #参数 关联模型
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    type=models.ForeignKey('type',on_delete=models.PROTECT,verbose_name='所属分类')
    tags=models.ManyToManyField('tags',related_name='tags',verbose_name='所属标签')
   

    def __str__(self):
        return  self.title
    def get_detail_url(self):
        return reverse('blogs:bloginfo',kwargs={'pk':self.pk})
    #增加阅读量
    def add_readnum(self):
        self.readnum+=1
        self.save(update_fields=['readnum'])
        #保存指定字段  提高数据库操作效率
    #增加评论量
    def add_commentsnum(self):
        self.comment_num+=1
        self.save(update_fields=['comment_num'])

    class Meta:
        verbose_name='博客信息'
        verbose_name_plural=verbose_name
class Comments(models.Model):
    status=(
        (1,'正常'),
        (2,'冻结')
    )
    content=models.CharField(max_length=255,verbose_name='评论内容')
    status=models.IntegerField(choices=status,verbose_name='状态',default=1)
    createtime=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    # 需要外键关联的字段
    # 评论人  ，评论的上一级，被评论人，被评论博客
    senduser=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name='评论人',related_name='senduser')
    acceptparent=models.ForeignKey('self',on_delete=models.PROTECT,verbose_name='上一级',related_name='accpet',blank=True,null=True)
    targetuser=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='接受评论人',related_name='acceptuser',blank=True,null=True)
    blog=models.ForeignKey('blogs',on_delete=models.PROTECT,verbose_name='博客')
    def __str__(self):
        return  self.content
    class Meta:
        verbose_name='评论信息'
        verbose_name_plural=verbose_name