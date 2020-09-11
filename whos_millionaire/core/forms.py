from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationFormCustom(UserCreationForm):
    email = forms.EmailField(required=True,
                             label="Correo electrónico",
                             widget=forms.EmailInput(),)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationFormCustom, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
