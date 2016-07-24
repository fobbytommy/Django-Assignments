from __future__ import unicode_literals
from ..loginReg.models import User
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

class Course_category(models.Model):
	course_number = models.IntegerField()
	title = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Course_new(models.Model):
	user = models.ForeignKey(User)
	course_category = models.ForeignKey(Course_category)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
