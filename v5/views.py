from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, FormView

from v5.forms import MyForm


class IndexView(TemplateView):
    template_name = "v5/index.html"


class ResultView(View):
    template_name = "v5/result.html"

    def post(self, request, *args, **kwargs):
        result = {
            'name': request.POST['name'],
            'hobby': request.POST['hobby'],
        }
        return render(request, self.template_name, result)


class BasicFormView(FormView):
    template_name = 'v5/basic_form.html'
    form_class = MyForm
    success_url = 'done'

    def form_valid(self, form):
        return super().form_valid(form)


class DoneView(TemplateView):
    template_name = "v5/done.html"
