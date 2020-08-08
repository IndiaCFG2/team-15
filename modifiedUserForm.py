from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):
    board = forms.CharField(max_length=50)
    mob_number = forms.CharField(max_length=50)
    class Meta:
        model = User
        field = ("username","password1","password2","board","mob_number")

    def save(self , commit = True):
        user = super(NewUserForm,self).save(commit=False)
        user.board = self.cleaned_data['board']
        user.mob_number = self.cleaned_data['mob_number']
        if commit:
            user.save()
        return user
