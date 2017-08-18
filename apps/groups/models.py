from django.db import models
from django.utils import timezone
class User(models.Model):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	username = models.CharField(max_length=60)
	password = models.CharField(max_length=60)
	created_at = models.DateField(default=timezone.now())
class Group(models.Model):
	name = models.CharField(max_length=60)
	description = models.CharField(max_length=100)
	created_by = models.ForeignKey(User)
	created_at = models.DateField(default=timezone.now())
class Member(models.Model):
	user = models.ForeignKey(User)
	group = models.ForeignKey(Group)