from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("applab.html")
    return HttpResponse(template.render())

def game1(request):
    template = loader.get_template("game1.html")
    return HttpResponse(template.render())

def game2(request):
    template = loader.get_template("game2.html")
    return HttpResponse(template.render())