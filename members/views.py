from django.http import HttpResponseRedirect, request
from .forms import  EditProfilePageForm, UserRegisterForm, UserLoginForm, PasswordChangingForm, EditProfileForm, ProfilePageForm, AboutPageForm, EditAboutForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from theblog.models import About, Profile
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

# Create your views here.
class AboutFormView(CreateView):
    model = About
    form_class = AboutPageForm
    template_name = 'registration/create_about.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class AboutFormUpdateView(UpdateView):
    model = About
    form_class = EditAboutForm
    template_name = 'registration/edit_about.html'

class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile.html'
    #fields = '__all__'
    
   
class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    success_url = reverse_lazy('home')

class ProfileView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    def get_context_data(self,*args, **kwargs):
        users=Profile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

def successPassword(request):
    return render(request, 'registration/success_password.html')

class PasswordsChangerView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/password_changer.html'
    success_url = reverse_lazy('success_password')

class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    


class UserLogin(generic.CreateView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/user_edit.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)