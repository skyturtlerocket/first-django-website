from django.http import HttpResponse
from django.template import loader

def aboutcreator2(request):
    template = loader.get_template('aboutcreator2.html')
    return HttpResponse(template.render())