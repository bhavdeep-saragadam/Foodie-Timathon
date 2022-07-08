from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
# Create your models here.


class Todo(models.Model):
	owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL) 
	todo = models.CharField(max_length=200)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
	
	class Meta:
		ordering = ['-todo']

class TodoPage(models.Model):
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	