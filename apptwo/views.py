from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.
def djangorocks(request):
    return HttpResponse("This is a Jazzy Response")


def picture_detail(request, category, year=0, month=0, day=0):
    template = loader.get_template('apptwo/index.html')


    context = {
     'pictures': [
         {
             'name': 'Spiderman',
             'filename': 'amaing_spider_man.jpg'
         },
         {
             'name': 'WallHaven',
             'filename': 'wallhaven-25690.jpg'
         },
     ]
    }
    return HttpResponse(template.render(context, request))



