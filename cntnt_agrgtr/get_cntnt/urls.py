from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
app_name = "get_cntnt"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:cat>', views.index, name = 'cat'),


    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('addlove/', views.add_to_lovelist, name='addtolovelist'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="get_cntnt/reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="get_cntnt/reset_passoword_sent.html"), name="reset_password_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="get_cntnt/reset_passoword_form.html"), name="reset_password_confirm"),
    path('reset_password_complite/', auth_views.PasswordResetCompleteView.as_view(template_name="get_cntnt/reset_password_done.html"), name="reset_password_complete"),

    path('profile/', views.profile, name='profile'),


]