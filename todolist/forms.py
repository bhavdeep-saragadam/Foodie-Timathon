from django import forms

from django.forms import ModelForm

from .models import Todo




class TodoForm(ModelForm):
	class Meta:
		model = Todo
		fields = ['todo']
	def __init__(self, *args, **kwargs):

		super(TodoForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			field.widget.attrs.update({'class':'form-control'})
			self.fields['todo'].widget.attrs.update({'placeholder': 'eg.. Eat Healthy Food REMEMBER YOU CANT DELETE OR EDIT THIS AFTER😁'})