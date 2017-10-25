from django.conf.urls import url

from account.views import LoginView, HomeView, LogoutView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
