from django.conf.urls import url

from account.views import LoginView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login')
]
