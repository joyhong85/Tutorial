from django.http import HttpResponse
from django.shortcuts import render
# from django.views.generic.base import View
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

# 실은 request.method 를 통해 HTTP 방식에 따라 처리를 해준다.
# 이 예시는 함수형 뷰
def index(request):
    if request.method == 'GET':
        response = HttpResponse()
        response.write("<h1>Welcome</h1>")
        response.write("<p>This is my first Django. </p>")
        return response

# 이것을 클래스형 뷰로 변경
class BaseView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse()
        response.write("<h1>Welcome</h1>")
        response.write("<p>This is my first Django. </p>")
        return response

# def index(request):
#     return render(request, 'v2/index.html')
class IndexView(View):
    # template_name = "v2/index.html"
    # return render(request, 'v2/index.html')

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

# def name(request):
#     return render(request, 'v2/name.html', {'name':'Joy'})
@method_decorator(csrf_exempt, name='dispatch')
class NameView(TemplateView):
    template_name = "v2/name.html"

    def get_context_data(self, **kwargs):
        context = super(NameView, self).get_context_data(**kwargs)
        print(context)
        context['name'] = context['keyword']
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Your code here
        # Here request.POST is the same as self.request.POST
        # You can also access all possible self variables
        # like changing the template name for instance
        bar = self.request.POST.get('keyword', None)
        # if bar: self.template_name = 'v2/name.html'
        print("-"*100)
        print(context)
        print(type(context))
        # previous_foo = context['keyword']
        context['name'] = "POST TEST"
        print(context)
        return self.render_to_response(context)

# def username(request, keyword):
#     return render(request, 'v2/name.html', {'name':keyword})


# class TemplateView(TemplateResponseMixin, View):
#     template_name = 'some_app/some_template.html'
#     def get(self, request, *args, **kwargs):
#         context = get_context_from_somewhere(request, *args, **kwargs)
#         return self.render_to_response(request, context)

