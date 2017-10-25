# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView


class LoginView(FormView):
    success_url = '/home/'
    form_class = AuthenticationForm
    template_name = 'templates/login.html'

    def form_valid(self, form):
        login(form.request, form.get_user())

        return super(LoginView, self).form_valid(form)
