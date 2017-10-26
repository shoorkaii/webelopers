from django.conf.urls import url

from account.views import LoginView, HomeView, LogoutView, UserInfoView, BetterUserInfoView, ShowUserInfoView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^user-info/$', BetterUserInfoView.as_view(), name='user-info'),
    url(r'^all/$', ShowUserInfoView.as_view(), name='all'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
