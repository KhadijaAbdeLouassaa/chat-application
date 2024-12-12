from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth
app_name = "accounts"


urlpatterns = [

    path('settings/', views.settings, name = "settings"),
    path('edit-profile/',views.EditProfile.as_view(), name = "edit_profile"),
    
    path('signup/', views.Signup.as_view(), name= "signup"),
	path('login/', auth.LoginView.as_view(template_name="accounts/registration/login.html"), name= "login"),
	path('logout/', auth.LogoutView.as_view(), name= "logout"),
    
    
    # - section of reset password  
    
    path('password-reset/', auth.PasswordResetView.as_view(template_name="accounts/registration/password_reset.html", 
    email_template_name="accounts/registration/password_reset_email.html",success_url=reverse_lazy("accounts:password_reset_done")),name= "password_reset"),
    
    path('password-reset/done/', auth.PasswordResetDoneView.as_view(template_name="accounts/registration/password_reset_done.html"),
    name= "password_reset_done"),
    
    path('reset/<uidb64>/<token>/',auth.PasswordResetConfirmView.as_view(template_name="accounts/registration/password_reset_confirm.html",success_url=reverse_lazy("accounts:password_reset_complete")),
    name="password_reset_confirm"),
    
    path('reset/done/',auth.PasswordResetCompleteView.as_view(template_name="accounts/registration/password_reset_complete.html"),
    name="password_reset_complete")

    
    
    
]