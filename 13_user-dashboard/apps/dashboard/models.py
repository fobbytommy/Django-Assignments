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
			return (True, 'Successfully registered! <3', user.id, user.user_level)

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

	def user_total_update(self, info, user_id):
		first_name = str(info['first_name'])
		last_name = str(info['last_name'])
		user_level = info['user_level']
		email = info['email']

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
			if User.objects.get(id=user_id).email != email:
				if User.objects.get(email=email):
					errors.append('Same email already exist!')
		except:
			pass

		if errors:
			return (False, errors)
		else:
			user = User.objects.get(id=user_id)
			user.first_name = first_name
			user.last_name = last_name
			user.email = email
			user.user_level = user_level
			user.save()
			return (True, 'Successfully updated!')

	def email_name_update(self, info, user_id):
		first_name = str(info['first_name'])
		last_name = str(info['last_name'])
		email = info['email']

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
			if User.objects.get(id=user_id).email != email:
				if User.objects.get(email=email):
					errors.append('Same email already exist!')
		except:
			pass

		if errors:
			return (False, errors)
		else:
			user = User.objects.get(id=user_id)
			user.first_name = first_name
			user.last_name = last_name
			user.email = email
			user.save()
			return (True, 'Successfully updated!')


	def password_update(self, info, user_id):
		password = info['password']
		confirm_pw = info['confirm_pw']
		errors = []
		if len(password) < 8:
			errors.append('Password should be longer than 8 characters!')
		elif password != confirm_pw:
			errors.append('Your password does not match the confirmed password!')

		if errors:
			return (False, errors)
		else:
			hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			user = User.objects.get(id=user_id)
			user.password = hashed_pw
			user.save()
			return (True, 'Successfully updated your password!')

	def description_update(self, info, user_id):
		description = str(info['description'])
		errors = []
		if len(description) > 500:
			errors.append('Description cannot be over 500 characters! Keep it shorter!')

		if errors:
			return (False, errors)
		else:
			user = User.objects.get(id=user_id)
			user.description = description
			user.save()
			return (True, 'Successfully updated your description!')

class messageManager(models.Manager):
	def add_message(self, message, to_who, user_id):
		errors = []
		if len(str(message)) < 10:
			errors.append("Please put more than 10 characters!")
		elif  len(str(message)) > 500:
			errors.append("Please put less than 500 characters!")

		if errors:
			return (False, errors)
		else:
			Message.objects.create(message = message, user_id = user_id, to_who = to_who)
			return (True, "Successfully added a new message!")
	def retrieve_message(self, user_id):
		data_1 = User.objects.get(id=user_id)
		data_2 = User.objects.raw("SELECT dashboard_user.id, dashboard_user.first_name, dashboard_user.last_name, dashboard_message.created_at, dashboard_message.message, dashboard_message.id AS 'message_id' FROM dashboard_user JOIN dashboard_message ON dashboard_user.id = dashboard_message.user_id WHERE dashboard_message.to_who = {} ORDER BY dashboard_message.created_at DESC".format(user_id))
		# Message.objects.get(to_who=user_id)
		return (data_1, data_2)

class postManager(models.Manager):
	def add_post(self, post, message_id, user_id):
		errors = []
		if len(str(post)) < 10:
			errors.append("Please put more than 10 characters!")
		elif  len(str(post)) > 500:
			errors.append("Please put less than 500 characters!")

		if errors:
			return (False, errors)
		else:
			Post.objects.create(post = post, message_id = message_id, user_id = user_id)
			return (True, "Successfully added a new post!")
	def retrieve_post(self, user_id):
		messages = Message.objects.raw("SELECT dashboard_message.id FROM dashboard_message WHERE to_who = {}".format(user_id))
		message_ids = ""
		for message in messages:
			message_ids += str(message.id) + ", "
		message_ids = message_ids[:-2]
		posts = Post.objects.raw("SELECT dashboard_post.id, dashboard_user.first_name, dashboard_user.last_name, dashboard_post.post, dashboard_post.created_at, dashboard_post.user_id, dashboard_post.message_id FROM dashboard_post JOIN dashboard_user ON dashboard_post.user_id = dashboard_user.id WHERE dashboard_post.message_id IN ({})".format(message_ids))
		return posts
class User(models.Model):
	first_name = models.CharField(max_length=100)
 	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	user_level = models.IntegerField()
	hashed_pw = models.CharField(max_length=255) # hashed password
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	description = models.TextField(max_length=500)
	userManager = UserManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
	# *************************

class Message(models.Model):
	message = models.TextField(max_length=500)
	user = models.ForeignKey(User)
	to_who = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	messageManager = messageManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
	# *************************

class Post(models.Model):
	post = models.TextField(max_length=500)
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	postManager = postManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
	# *************************
