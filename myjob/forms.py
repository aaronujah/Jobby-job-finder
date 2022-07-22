from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Company, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website', 'logo']
        exclude = ['user']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'avatar', 'bio', 
        'interest_one', 'interest_two', 'interest_three' ]
        