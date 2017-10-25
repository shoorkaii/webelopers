from django.conf.urls import url

from backend.account.views import LoginView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login')
]
