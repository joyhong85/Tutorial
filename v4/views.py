import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

# v1 버전에서 만든 것
# def index(request):
#     response = HttpResponse()
#     response.write("<h1>Welcome</h1>")
#     response.write("<p>This is my first Django. </p>")
#     return response

# 실제로는 request.method 를 통해 HTTP 방식에 따라 처리를 해준다.
# 이 예시는 함수형 뷰
# def index(request):
#     if request.method == 'GET':
#         response = HttpResponse()
#         response.write("<h1>Welcome</h1>")
#         response.write("<p>This is my first Django. </p>")
#         return response

# 이것을 클래스형 뷰로 변경한 것
class BaseView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse()
        response.write("<h1>Welcome</h1>")
        response.write("<p>This is my first Django. </p>")
        return response


class IndexView(View):
    template_name = "v2/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class HtmlView(TemplateView):
    template_name = "v3/index.html"


@method_decorator(csrf_exempt, name='dispatch')
class NameView(TemplateView):
    template_name = "v2/name.html"

    def get_context_data(self, **kwargs):
        context = super(NameView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        """
        GET 방식으로 요청이 들어오면 URL에 입력된 값을 context에 담아 template_name에 해당되는 html을 렌더링하도록 처리한다.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, **kwargs):
        """
        POST 방식으로 들어오면 body의 내용을 context에 담아 template_name에 해당되는 html을 렌더링하도록 처리한다.
        :param request:
        :param kwargs:
        :return:
        """
        context = self.get_context_data(**kwargs)
        try:
            body = json.loads(request.body.decode('utf8'))
            context['name'] = body['keyword']
        except:
            pass
        return self.render_to_response(context)

