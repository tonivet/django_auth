from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import UserProfile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First name", max_length=55, widget=forms.TextInput(attrs={'class':'form-control '}))
    last_name = forms.CharField(label="Last name", max_length=55, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = "" #'<span class="form-text text-muted"><small>This field is required.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = "" # '<ul class="form-text text-muted"><li><small>Your password must contain at least 8 characters.</small></li><li><small>Your password can\'t be entirely numeric.<small></li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = 'Retype password'
        self.fields['password2'].help_text = "" #'<span class="form-text text-muted"><small>Type your password as before, for verification.</small></span>'
    

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileUpdateForm(forms.ModelForm):
    sex = forms.ChoiceField(choices=UserProfile.SEX_CHOICES, required=False)
    city = forms.CharField(required=False)
    country = forms.CharField(required=False)
    class Meta:
        model = UserProfile
        fields = ['image', 'sex', 'city', 'country']

