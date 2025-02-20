from django.contrib import admin

# Register your models here.
#将模型注册到后台管理
from .models import *

#修改admin界面中显示的字段或者筛选过滤  或者搜索
#分类管理  列表显示名称，说明
# 创建配置管理器类
class TypeAdmin(admin.ModelAdmin):
    list_display=('name','describe')
class BlogsAdmin(admin.ModelAdmin):
    list_display=('title','abstract','type','readnum','comment_num')
    list_filter=('type','readnum')
    list_editable=('type','readnum')
    ordering=('readnum','comment_num')
admin.site.register(Type,TypeAdmin)
admin.site.register(Tags)
admin.site.register(Blogs,BlogsAdmin)
admin.site.register(Comments)
admin.site.site_header="博客管理系统"
admin.site.site_title="博客管理系统"

# 练习  相关博客管理  将标签管理、评论管理  按照文章管理格式修改
#      将用户管理添加到后台admin页面中

