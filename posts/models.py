from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Post(models.Model):
	owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL) 
	title = models.CharField(max_length=200)
	featured_image = models.ImageField(null=True, blank=True, default="defualt.jpg")
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ['-created']

 
