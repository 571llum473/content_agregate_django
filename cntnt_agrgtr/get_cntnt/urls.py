from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, UserSetPassowrdForm

from . import views
urlpatterns = [
#Home Page
    path('', views.index, name='home'),
    path('<str:cat>', views.category, name = 'cat'),

#Registration
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

#Password reset
    path('reset_password/',
        auth_views.PasswordResetView.as_view(
            template_name="get_cntnt/password_reset.html",
            form_class=UserPasswordResetForm,),
        name="reset_password"),

    path('reset_password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="get_cntnt/password_reset_sent.html",),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="get_cntnt/password_reset_form.html",
            form_class=UserSetPassowrdForm),
        name="password_reset_confirm"),

    path('reset_password/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="get_cntnt/password_reset_done.html",),
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