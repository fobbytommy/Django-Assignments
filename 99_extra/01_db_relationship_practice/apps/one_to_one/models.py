from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogManager(models.Manager):
	def add_blog(self, data):
		title = data['title']
		description = data['description']
		blog = Blog.objects.create(title = title)
		print blog.id
		Description.objects.create(description = description, blog_id = blog.id)
		return None

class Blog(models.Model):
	title = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	blogManager = BlogManager()
	objects = models.Manager()

class Description(models.Model):
	description = models.TextField(max_length = 1000)
	blog = models.OneToOneField(Blog)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
