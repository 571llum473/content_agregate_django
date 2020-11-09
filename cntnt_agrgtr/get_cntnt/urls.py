from django.urls import path

from . import views
app_name = "get_cntnt"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:cat>', views.index, name = 'cat'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
]