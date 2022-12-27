from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import UserLoginForm, UserRegistrationForm


class UserSignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        instance = form.save()
        my_group = Group.objects.get(name='Doctors')
        my_group.user_set.add(instance)
        return super().form_valid(form)


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    success_url = reverse_lazy('products')
