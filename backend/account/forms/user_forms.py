from django.forms.models import ModelForm

from account.models import UserInfo


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('phone_number', 'address', 'profile_picture')
