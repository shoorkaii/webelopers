# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.list import ListView

from account.forms.user_forms import UserInfoForm
from account.models import UserInfo


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


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'post.html'
    login_url = '/'


class UserInfoView(LoginRequiredMixin, FormView):
    form_class = UserInfoForm
    template_name = 'form.html'

    def get_initial(self):
        initial = super(UserInfoView, self).get_initial()
        if self.request.user.additionals.count() > 0:
            user_info = self.request.user.additionals.all()[0]
            initial['phone_number'] = user_info.phone_number
            initial['address'] = user_info.address
            initial['profile_picture'] = user_info.profile_picture
        return initial

    def form_valid(self, form):
        if self.request.user.additionals.count() > 0:
            user_info = self.request.user.additionals.all()[0]
            user_info.phone_number = form.data['phone_number']
            user_info.save()
        else:
            user_info = UserInfo()
            user_info.user = self.request.user
            user_info.phone_number = form.data['phone_number']
            user_info.save()
        return super(UserInfoView, self).form_valid(form)


# TODO: see CreateView later
class BetterUserInfoView(LoginRequiredMixin, UpdateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'form.html'
    success_url = '/user-info/'

    def get_object(self, queryset=None):
        if self.request.user.additionals.count() > 0:
            return self.request.user.additionals.all()[0]
        return None


# TODO: see DetailView later
class ShowUserInfoView(LoginRequiredMixin, ListView):
    model = UserInfo
    template_name = 'all.html'

    def get_queryset(self):
        return UserInfo.objects.filter(user=self.request.user).order_by('phone_number')

    # See template variables
    # def get_context_data(self, **kwargs):
    #     context = super(ShowUserInfoView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context
