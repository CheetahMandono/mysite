from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# class RegisterForm(UserCreationForm):
#     # declare the fields you will show
#     username = forms.CharField(label="Your Username")
#     # first password field
#     password1 = forms.CharField(label="Your Password", widget=forms.PasswordInput)
#     # confirm password field
#     password2 = forms.CharField(label="Repeat Your Password", widget=forms.PasswordInput)
#     email = forms.EmailField(label="Email Address")
#
#     # this sets the order of the fields
#     class Meta:
#         model = User
#         fields = ("email", "username", "password1", "password2",)
#
#     # this redefines the save function to include the fields you added
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#
#         if commit:
#             user.save()
#             return user

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
