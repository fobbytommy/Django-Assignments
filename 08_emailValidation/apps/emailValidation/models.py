from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UserManager(models.Manager):
	def email(self, email):
		if len(email) < 1:
			return (False, 'Email cannot be blank!')
			# if email doesn't match regular expression,
			# display an "invlaid email address" message.
		elif not EMAIL_REGEX.match(email):
			return (False, 'Invalid Email Address!')
		else:
			return(True, 'The email address you entered {} is a VALID email address! Thank you!'.format(email))
# Create your models here.
class Email(models.Model):
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# *************************
	# Connect an instance of UserManager to our User model!
	userManager = UserManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
	# *************************
