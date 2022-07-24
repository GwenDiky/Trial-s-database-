from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="Почта",widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="Имя",max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Фамилия", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'