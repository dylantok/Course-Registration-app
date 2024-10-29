from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Profile


class SignUpForm(UserCreationForm):#Django標準の登録フォーム
    email = forms.EmailField(required=True,
        label=_("メールアドレス"),
        error_messages={'required': _("メールアドレスは必須です。")}
        )
    
    school_year_choices = [
        ('1', '1年'),
        ('2', '2年'),
        ('3', '3年'),
        ('4', '4年')
    ]
    school_year = forms.ChoiceField(
        choices=school_year_choices,
        required=True,
        label=_("学年"),
        initial='1'
    )

    undergraduate_choices = [
        ('management', '経営学部'),
        ('commerce', '商学部'),
        ('human_sciences', '人間科学部')
    ]
    undergraduate = forms.ChoiceField(
        choices=undergraduate_choices,
        required=True,
        label=_("学部"),
        initial='management'
    )
    course_choices = [
        ('', '---------'),  # デフォルトの空選択肢
        ('corporate_management', '企業経営'),
        ('management_law', '経営法務'),
        ('Entrepreneurship_and_Business_Succession', '起業・事業承継'),
        ('information', '情報'),
        ('finance', '金融'),
        ('accounting', '会計'),
        ('marketing', 'マーケティング'),
        ('psychology', '人間科学専攻（心理・コミュニケーションコース）'),
        ('sociology', '人間科学専攻（社会・ライフデザインコース）'),
        ('Child_Education', '児童教育専攻')
    ]
    course = forms.ChoiceField(
        choices=course_choices,  # JavaScriptで動的に設定するためデフォルトは空
        required=False,
        label=_("コース"),
    )
    english_class_choice = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    english_class = forms.ChoiceField(
        choices=english_class_choice,
        required=True,
        label=_("英語クラス"),
        initial='1'
    )
    repeating_a_course_choice = [
        ('あり', 'あり'),
        ('なし', 'なし')
    ]
    repeating_a_course = forms.ChoiceField(
        choices=repeating_a_course_choice,
        required=True,
        label=_("再履修"),
        initial='1'
    )
    First_and_second_terms_semester_choice = [
        ('前期', '前期'),
        ('後期', '後期')
    ]
    First_and_second_terms_semester = forms.ChoiceField(
        choices=First_and_second_terms_semester_choice,
        required=True,
        label=_("前期・後期"),
        initial='1'
    )
    Seminar_membership_choice = [
        ('加入', '入っている'),
        ('未加入', '入っていない')
    ]
    Seminar_membership = forms.ChoiceField(
        choices=Seminar_membership_choice,
        required=True,
        label=_("ゼミ加入の有無"),
        initial='1'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','school_year','undergraduate','course','english_class','repeating_a_course','First_and_second_terms_semester','Seminar_membership')
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
        # プロフィールを保存
        profile = Profile.objects.create(
            user=user,
            school_year=self.cleaned_data['school_year'],
            undergraduate=self.cleaned_data['undergraduate'],
            course=self.cleaned_data['course'],
            english_class=self.cleaned_data['english_class'],
            repeating_a_course=self.cleaned_data['repeating_a_course'],
            First_and_second_terms_semester=self.cleaned_data['First_and_second_terms_semester'],
            Seminar_membership=self.cleaned_data['Seminar_membership']
        )
        return user

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': "ユーザー名",
            'email': "メールアドレス",
        }

class EditProfileExtraForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['school_year', 'undergraduate', 'course','english_class','repeating_a_course','First_and_second_terms_semester','Seminar_membership']
        labels = {
            'school_year': "学年",
            'undergraduate': "学部",
            'course': "コース",
            'english_class': "英語クラス",
            'repeating_a_course': "再履修",
            'First_and_second_terms_semester':  "前期・後期",
            'Seminar_membership': "ゼミ加入の有無"
        }