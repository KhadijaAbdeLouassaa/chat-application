from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Profile
from .forms import SignupForm,EditProfileForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
# Create your views here.


class Signup(CreateView):
	form_class = SignupForm
	template_name = "accounts/signup.html"
	success_url = reverse_lazy("accounts:login")
    
    
class EditProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = "accounts/edit_profile.html"
    success_url = "/"
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
   

@login_required
def settings(request):
    user_profile = Profile.objects.filter(user=request.user)
    
    return render(request,"accounts/settings.html",{'user_profile':user_profile})



@receiver(user_logged_in)
def online_user(sender,request, user, **kwargs):
    user = Profile.objects.filter(user=user).update(is_active = True)
    
@receiver(user_logged_out)   
def offline_user(sender,request,user, **kwargs):
    user = Profile.objects.filter(user=user).update(is_active = False)
    
















