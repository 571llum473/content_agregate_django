from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
app_name = "get_cntnt"
urlpatterns = [
#Home Page
    path('', views.index, name='index'),
    path('<str:cat>', views.category, name = 'cat'),

#Registration
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

#Password reset
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="get_cntnt/reset_password.html"), 
        name="reset_password"),
    
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="get_cntnt/reset_passoword_sent.html"), 
        name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="get_cntnt/reset_passoword_form.html"), 
        name="password_reset_confirm"),
    
    path('reset_password_complite/',
     auth_views.PasswordResetCompleteView.as_view(template_name="get_cntnt/reset_password_done.html"), 
     name="password_reset_complete"),
    
#Profile Model
    path('favourite/', views.favourite, name='favourite'),
    path('profile/', views.profile, name='profile'),
    path('addlove/', views.add_to_lovelist, name='addtolovelist'),

#Password Change
    path('profile/change_password/', views.change_password, name="change_password"),
    path('profile/change_password/done', views.change_password_done, name="change_password_done"),
    

    path('profile/profile_change/', views.profile_change, name='profile_change')



]