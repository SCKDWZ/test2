from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib import auth
User=get_user_model()
def Login(request):
    #登录 
    #首先get拿到登录页面 输入用户名密码使用post请求发送
    #服务器拿到数据之后 校验用户名密码 成功返回首页 不成功返回错误信息
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        try:
            username=request.POST['logname']
            password=request.POST['logpass']
            #查找用户
            user=User.objects.get(username=username)
            #校验密码
            if user.check_password(password):
                auth.login(request,user)
                return render(request,'index.html')
            else:
                return render(request,'login.html',context={"login_result":'password  error'})
        except Exception as e:
            login_result=str(e)
            context={'login_result':login_result}
            return render(request,'login.html',context=context)

#半个小时 将登录功能测试完成