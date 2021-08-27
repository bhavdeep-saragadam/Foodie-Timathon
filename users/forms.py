from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class User(UserCreationForm):
	class Meta:
		model = User
		fields =  ['username','password1','password2']
	def __init__(self, *args, **kwargs):

		super(User, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			field.widget.attrs.update({'class':'form-control'})
