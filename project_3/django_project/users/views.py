from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm ,UserLoginForm
from django.http import HttpResponse
from django.views.generic import View
from django.views import View
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, RedirectView, TemplateView

from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User, auth
from django.utils.encoding import smart_str

from django.contrib.auth.views import LoginView


class RegisterView(View):
    form_class = UserRegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    
    def get(self,request,*args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        """ Register a user """
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exists')
                    return redirect('register')
            # import pdb; pdb.set_trace()
           
            messages.success(request, f' {username} Your account has been created! Kindly confirm the mail to log in  !')
            return redirect('login')


class Profile (View):
    user_form = UserUpdateForm
    profile_form = ProfileUpdateForm
    template_name = 'users/profile.html'

    @method_decorator(login_required)
    def get(self,request,*args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        """ post user profile and update profile it"""
        post_data = request.POST or None
        file_data = request.FILES or None
        u_form = UserUpdateForm(post_data,  instance=request.user)
        p_form = ProfileUpdateForm(post_data, file_data , instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')


 
class Login(LoginView):
    """
    Provides users the ability to login
    """
    authentication_form = UserLoginForm
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        print(form.get_user().is_email_verified)
        if form.get_user() and not form.get_user().is_email_verified:
            messages.info(self.request, 'Email is not verified, please check your email inbox')
            return render(self.request, 'accounts/login.html')
        # login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:main')
