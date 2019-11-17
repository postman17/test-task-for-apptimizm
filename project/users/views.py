from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import UserProfile
from .forms import UserForm, UserProfileForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(user=self.request.user).first()
        return context


class RegistrationView(TemplateView):
    template_name = 'registration.html'

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['user_form'] = UserForm(self.request.POST or None)
        context['profile_form'] = UserProfileForm(self.request.POST or None)
        return context

    def post(self, request):
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
        context = self.get_context_data()
        return self.render_to_response(context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile-edit.html'
    success_url = reverse_lazy('profile')
