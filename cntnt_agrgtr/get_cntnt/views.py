from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Source

# Create your views here.
def index(request, cat=None):
    if cat:
        sources = Source.objects.filter(category=cat)
    else:
        sources = Source.objects.all()
    latest_news = {i : i.news_set.order_by('-pub_time')[:5] for i in sources}
    cat_choices = {i[0] : i[1] for i in Source.CAT_CHOICES}
    context = {
        'latest_news' : latest_news,
        'CAT_CHOICES' : cat_choices
    }
    return render(request, 'get_cntnt/index.html', context)
