from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from AnalyticsApp.forms import SignUpForm

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'