from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def index(request):
    """进入首页"""
    print('=====index视图函数====')

    aa = None
    print('aa='+aa)
    return render(request, 'index.html')

def show_static(request):
    return render(request,'show_static.html')


def upload(request):


    return render(request,'upload.html')

def do_upload(request):

    # 获取上传对象
    pic = request.FILE.get('pic')




