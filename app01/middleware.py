from django.http import HttpResponse


class MyMiddleware(object):
    def __init__(self):
        print('---init----')

    def process_request(self, request, ):
        print('----process_request-----')
        # exclude_ips =['127.0.0.1']
        # # 获取ip
        # ip = request.META.get('REMOTE_ADDR')
        # if ip in exclude_ips:
        #     return HttpResponse('禁止访问')

    def process_exception(self, request, exception):
        print('-----process_exception')
        return HttpResponse('运行出错了：%s' %exception)

    def process_view(self,request, view_func, view_args, view_kwargs):
        print('----process_view----')

    def process_response(self,request, response):
        print('----process_response----')
        return response


