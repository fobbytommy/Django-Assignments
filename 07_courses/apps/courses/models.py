from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Description(models.Model):
	description = models.TextField(max_length=500)
	course = models.OneToOneField(
		Course,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
	course = models.ForeignKey(Course)
	comment = models.TextField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
