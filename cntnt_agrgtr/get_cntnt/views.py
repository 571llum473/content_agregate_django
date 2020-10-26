from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Source

# Create your views here.
def index(request):
    sources = Source.objects.all()
    template = loader.get_template('get_cntnt/index.html')
    latest_news = {i : i.news_set.order_by('-pub_time')[:5] for i in sources}
    context = {
        'latest_news' : latest_news,
    }
    return HttpResponse(template.render(context, request))