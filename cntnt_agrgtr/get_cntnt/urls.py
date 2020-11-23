from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
#Home Page
    path('', views.homePage, name='home'),
    path('<str:cat>', views.homePage, name='cat'),

#Registration
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

#Password reset
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="get_cntnt/password_reset.html"), 
        name="reset_password"),
    
    path('reset_password/', 
        auth_views.PasswordResetDoneView.as_view(template_name="get_cntnt/password_reset_sent.html"), 
        name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="get_cntnt/password_reset_form.html"), 
        name="password_reset_confirm"),
    
    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="get_cntnt/password_reset_done.html"), 
        name="password_reset_complete"),
  
#Profile Model
    path('favourite/', views.favourite, name='favourite'),
    path('profile/', views.profile, name='profile'),
    path('addlove/', views.add_to_lovelist, name='addtolovelist'),

#Password Change
    path('profile/change/password/', views.password_change, name="password_change"),
    path('profile/change/password/done', views.password_change_done, name="password_change_done"),    
    path('profile/change/', views.profile_change, name='profile_change')



]