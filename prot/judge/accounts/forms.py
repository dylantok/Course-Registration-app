from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):#Django標準の登録フォーム
    email = forms.EmailField(required=True,
        label=_("メールアドレス"),
        error_messages={'required': _("メールアドレスは必須です。")})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': _("ユーザー名"),
            'password1': _("パスワード"),
            'password2': _("パスワード確認"),
        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
