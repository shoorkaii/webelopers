# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class LoginView(FormView):
    success_url = '/home/'
    form_class = AuthenticationForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)


class HomeView(TemplateView):
    template_name = 'home.html'
