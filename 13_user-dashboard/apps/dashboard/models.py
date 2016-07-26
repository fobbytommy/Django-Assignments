from __future__ import unicode_literals
from django.db import models

# Create your models here.
import re
import bcrypt
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UserManager(models.Manager):
	def register(self, info):
		first_name = str(info['first_name'])
		last_name = str(info['last_name'])
		email = info['email']
		password = info['password']
		confirm_pw = info['confirm_pw']
		errors = []
		if len(first_name) < 2:
			errors.append('You first name is too short! Please put more than 2 characters!')
		elif len(first_name) > 100:
			errors.append('You first name is too long! Please keep it under 100 characters!')
		elif str.isalpha(first_name) != True:
			errors.append('Your first name should only contain alphabets!')
		if len(last_name) < 2:
			errors.append('Your last name is too short! Please put more than 2 characters!')
		elif len(last_name) > 100:
			errors.append('You last name is too long! Please keep it under 100 characters!')
		elif str.isalpha(last_name) != True:
			errors.append('Your last name should only contain alphabets! No spaces or symbols')
		if len(email) < 1:
			errors.append('Email cannot be blank!')
			# if email doesn't match regular expression,
			# display an invlaid email address message.
		elif not EMAIL_REGEX.match(email):
			errors.append('Invalid Email Address!')
		try:
			if User.objects.get(email=email):
				errors.append('Same email already exist!')
		except:
			pass
		if len(password) < 8:
			errors.append('Password should be longer than 8 characters!')
		elif password != confirm_pw:
			errors.append('Your password does not match the confirmed password!')

		if errors:
			return (False, errors)
		else:
			hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			if User.objects.all():
				User.objects.create(first_name = first_name, last_name = last_name, email = email, hashed_pw = hashed_pw, user_level = 1)
			else:
				User.objects.create(first_name = first_name, last_name = last_name, email = email, hashed_pw = hashed_pw, user_level = 9)
			user = User.objects.get(email=email)
			return (True, 'Successfully registered! <3', user.id)

	def login(self, info):
		errors = []
		email = info['email']
		password = info['password']
		try:
			user = User.objects.get(email=email)
			if bcrypt.hashpw(password.encode(), user.hashed_pw.encode()) != user.hashed_pw:
				errors.append('Your password is probably wrong.')
		except:
			errors.append('Not existing email. Please register!')

		if errors:
			return (False, errors)
		else:
			return (True, 'Successfully logged in! <3' , user.id)

class User(models.Model):
	first_name = models.CharField(max_length=100)
 	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	user_level = models.IntegerField()
	hashed_pw = models.CharField(max_length=255) # hashed password
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = UserManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
	# *************************

class Message(models.Model):
	message = models.TextField(max_length=500)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
	post = models.TextField(max_length=500)
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
