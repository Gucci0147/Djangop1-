from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'})) 
		
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class']='form-control' 
		self.fields['password1'].widget.attrs['class']='form-control' 
		self.fields['password2'].widget.attrs['class']='form-control' 

class EditProfileForm(UserChangeForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='', widget=forms.TextInput(attrs={'type': 'hidden'}))  
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')