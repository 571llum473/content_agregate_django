from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Source
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

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

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request, 'registration/register.html', context)

def login(request):
    context = {}
    return render(request, "registration/login.html", context)