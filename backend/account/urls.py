from django.conf.urls import url

from account.views import LoginView, HomeView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^home/$', HomeView.as_view(), name='home'),
]
