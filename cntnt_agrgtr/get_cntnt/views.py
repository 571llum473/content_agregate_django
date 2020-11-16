from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template import loader
from .models import Source
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def index(request, cat=None):
    if cat:
        sources = Source.objects.filter(category=cat)
    else:
        sources = Source.objects.all()

    search_querry = request.GET.get('search', '')
    if search_querry:
        sources = Source.objects.filter(name__icontains=search_querry)
    else:
        sources = Source.objects.all()
        
    latest_news = {i : i.news_set.order_by('-pub_time')[:5] for i in sources}
    cat_choices = {i[0] : i[1] for i in Source.CAT_CHOICES}
    context = {
        'latest_news' : latest_news,
        'CAT_CHOICES' : cat_choices
    }
    return render(request, 'get_cntnt/index.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('get_cntnt:index')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('get_cntnt:index')

    context = {"form":form}
    return render(request, 'get_cntnt/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('get_cntnt:index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('get_cntnt:index')
        else:
            messages.error(request,'Не правильный логин или пароль')

    context = {}
    return render(request, "get_cntnt/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('get_cntnt:index')

def profile(request):
    context = {}
    return render(request, 'get_cntnt/publications.html', context)