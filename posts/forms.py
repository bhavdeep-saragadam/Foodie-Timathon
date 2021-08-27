from django import forms
from .models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title','description','featured_image']
	def __init__(self, *args, **kwargs):

		super(PostForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			field.widget.attrs.update({'class':'form-control'})