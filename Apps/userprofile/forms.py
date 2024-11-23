from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=50, required=True)
	last_name = forms.CharField(max_length=50, required=True)
	email = forms.CharField(max_length=255, required=True)

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'w-full p-2 my-2 border-2 border-slate-300 focus:border-slate-600 outline-none'
		self.fields['first_name'].widget.attrs['class'] = 'w-full p-2 my-2 border-2 border-slate-300 focus:border-slate-600 outline-none'
		self.fields['last_name'].widget.attrs['class'] = 'w-full p-2 my-2 border-2 border-slate-300 focus:border-slate-600 outline-none'
		self.fields['email'].widget.attrs['class'] = 'w-full p-2 my-2 border-2 border-slate-300 focus:border-slate-600 outline-none'
		self.fields['password1'].widget.attrs['class'] = 'w-full p-2 my-2 border-2 border-slate-300 focus:border-slate-600 outline-none'
		self.fields['password2'].widget.attrs['class'] = 'w-full p-2 my-2 border-2 border-slate-300 focus:border-slate-600 outline-none'

		for field in ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']:
			self.fields[field].help_text = None

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
