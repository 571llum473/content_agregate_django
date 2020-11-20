from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template import loader
from .models import Source, Profile
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import RegisterForm, ChangeProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
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

def favourite(request):
    if request.user.is_authenticated:
        current_user = request.user
        profile = Profile.objects.get(user__username=current_user)
        sources = profile.love_list
        context = {"lovelist" : sources}
        return render(request, 'get_cntnt/favourite.html', context)
    else:
        return redirect('get_cntnt:index')

def add_to_lovelist(request):
    source_id = request.POST.get('source_id')
    current_user = request.user
    profile = Profile.objects.get(user__username=current_user)
    source = Source.objects.get(id = source_id)
    profile.love_list.add(source)
    return(HttpResponse('succes'))

def profile(request):
    user = request.user
    context = {"user" : user}
    return render(request, 'get_cntnt/profile.html', context)

def profile_change(request):
    user = request.user
    form = ChangeProfileForm(instance=user)
    if request.method == 'POST':
        form = ChangeProfileForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('get_cntnt:profile')

    context = {'form':form}
    return render(request, 'get_cntnt/profile_change.html', context)

def change_password(request):
    user = request.user
    form = PasswordChangeForm(user=user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('get_cntnt:change_password_done')
    context = {"form":form}
    return render(request, 'get_cntnt/change_password.html', context)

def change_password_done(request):
    return HttpResponse('<h1>Chnage password done</h1>')