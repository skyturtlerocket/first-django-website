from django.http import HttpResponse
from django.template import loader

def numbersense(request):
    template = loader.get_template("numbersense.html")
    return HttpResponse(template.render())

