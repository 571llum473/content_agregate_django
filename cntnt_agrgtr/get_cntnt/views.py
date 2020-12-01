from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Source, Profile
from .forms import RegisterForm, ChangeProfileForm, UserPasswordChangeForm

def index(request):
    """Home page view with news"""
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
    return render(request, 'get_cntnt/home.html', context)

def category(request, cat):
    """Categories view"""
    sources = Source.objects.filter(category=cat)
    latest_news = {i : i.news_set.order_by('-pub_time')[:5] for i in sources}
    cat_choices = {i[0] : i[1] for i in Source.CAT_CHOICES}
    context = {
        'latest_news' : latest_news,
        'CAT_CHOICES' : cat_choices
    }
    return render(request, 'get_cntnt/home.html', context)

def register_page(request):
    """Registration view with custom registration form RegisterForm(forms.py)"""
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    context = {"form":form}
    return render(request, 'get_cntnt/register.html', context)

def login_page(request):
    """Login view"""
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        messages.error(request,'Не правильный логин или пароль')

    context = {}
    return render(request, "get_cntnt/login.html", context)

def logout_user(request):
    """Logout user view"""
    logout(request)
    return redirect('home')

@login_required
def favourite(request):
    """Favourite news sites view"""
    current_user = request.user
    profile = Profile.objects.get(user__username=current_user)
    sources = profile.love_list
    context = {"lovelist" : sources}
    return render(request, 'get_cntnt/favourite.html', context)

def add_to_lovelist(request):
    """Ajax button to add to favorites"""
    source_id = request.POST.get('source_id')
    current_user = request.user
    profile = Profile.objects.get(user__username=current_user)
    source = Source.objects.get(id = source_id)
    profile.love_list.add(source)

@login_required
def profile(request):
    """User profile view"""
    user = request.user
    form = ChangeProfileForm(instance=user)
    if request.method == 'POST':
        form = ChangeProfileForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {"user" : user,
        'form':form}
    return render(request, 'get_cntnt/profile.html', context)

@login_required
def profile_change(request):
    """Change profile view with ChangeProfileForm(forms.py)"""
    user = request.user
    form = ChangeProfileForm(instance=user)
    if request.method == 'POST':
        form = ChangeProfileForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')

    context = {'form':form}
    return render(request, 'get_cntnt/profile_change.html', context)

@login_required
def password_change(request):
    """Change password view with UserPasswordChangeForm(forms.py)"""
    user = request.user
    form = UserPasswordChangeForm(user=user)
    if request.method == 'POST':
        form = UserPasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('password_change_done')
    context = {"form":form}
    return render(request, 'get_cntnt/password_change.html', context)

@login_required
def password_change_done(request):
    context = {}
    return render(request, 'get_cntnt/password_change_done.html', context)
