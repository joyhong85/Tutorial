from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse


# Create your views here.
def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("<p>This is my first Django. </p>")
    return response


def index_redirect(request):
    return HttpResponseRedirect('http://google.com')


def index_json(request):
    return JsonResponse({'key': 'value'})


def index_file(request):
    img = open('./images/IU_MelOn_Music_Awards_2017_06.jpg', 'rb')
    response = FileResponse(img)
    return response










# from django.shortcuts import render