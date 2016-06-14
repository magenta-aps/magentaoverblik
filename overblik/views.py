from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect('overblik:index')
        else:
            raise PermissionDenied()
