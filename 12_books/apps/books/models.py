from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UserManager(models.Manager):
	def register(self, info):
		name = str(info['name'])
		alias = str(info['alias'])
		email = info['email']
		password = info['password']
		confirm_pw = info['confirm_pw']
		errors = []
		if len(name) < 2:
			errors.append('You name is too short! Please put more than 2 characters!')
		elif len(name) > 100:
			errors.append('You name is too long! Please keep it under 100 characters!')
		elif str.isalpha(str(info['name'].replace(' ', ''))) != True:
			errors.append('Your name should only contain alphabets!')
		if len(alias) < 2:
			errors.append('Your alias is too short! Please put more than 2 characters!')
		elif len(alias) > 100:
			errors.append('You alias is too long! Please keep it under 100 characters!')
		elif str.isalpha(alias) != True:
			errors.append('Your alias should only contain alphabets! No spaces or symbols')
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
			User.objects.create(name = name, alias = alias, email = email, hashed_pw = hashed_pw)
			return (True, 'Successfully registered! <3')

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
			return (True, 'Successfully logged in! <3' , user.alias, user.id)

	def user_info(self, user_id):
		basic = User.objects.get(id=user_id)

		total_review = Review.objects.raw("SELECT books_review.id, COUNT(books_review.user_id) AS 'count_review' FROM books_review WHERE books_review.user_id = {} GROUP BY books_review.user_id".format(user_id))
		count_review = total_review[0].count_review

		review_list = Review.objects.raw("SELECT books_review.id, books_review.book_id, books_book.title FROM books_review JOIN books_book ON books_review.book_id = books_book.id WHERE books_review.user_id = {}".format(user_id))

		return (basic, count_review, review_list)
class reviewManager(models.Manager):
	def add_review(self, check_info, book_id, user_id):
		description = str(check_info['description'])
		rating = int(check_info['rating'])
		errors = []
		if len(description) < 30:
			errors.append('Please add review more than 30 characters long!')
		elif len(description) > 500:
			errors.append('Please keep your review under 500 characters!')

		if errors:
			return (False, errors)
		else:
			Review.objects.create(description = description, rating = rating, user_id = user_id, book_id = book_id)
			return (True, 'Successfully added a new book with your review!')

class bookManager(models.Manager):
	def new_book(self, book_info, user_id):

		title = str(book_info['title'])
		if len(str(book_info['author_new'])) > 1:
			author = str(book_info['author_new'])
		else:
			author = str(book_info['author_list'])
		author_temp = author
		description = str(book_info['description'])
		rating = int(book_info['rating'])

		errors = []

		if len(title) < 1:
			errors.append('Please add the title of the book!')
		elif len(title) > 200:
			errors.append('Please keep the title of the book fewer than 200 characters!')
		try:
			if Book.objects.get(title=title):
				errors.append('Same title already exist!')
		except:
			pass
		if len(author) < 1:
			errors.append('Please add the author of the book!')
		elif len(author) > 100:
			errors.append('Please keep the name of the author fewer than 100 characters!')
		elif str.isalpha(str(author_temp.replace(' ', ''))) != True:
			errors.append('Name of the author cannot contain numbers or symbols!')
		if len(description) < 30:
			errors.append('Please add review more than 30 characters long!')
		elif len(description) > 500:
			errors.append('Please keep your review under 500 characters!')

		if errors:
			return (False, errors)
		else:
			Book.objects.create(title = title, author = author)
			book = Book.objects.get(title = title, author = author)
			Review.objects.create(description = description, rating = rating, book_id = book.id, user_id = user_id)
			return (True, 'Successfully added a new book with your review!', book.id)
	def getting_info(self, book_id):
		book_data = Book.objects.raw("SELECT books_book.id, books_book.title, books_book.author, books_review.description, books_review.rating, books_review.id AS 'review_id', books_user.id AS 'user_id', books_user.alias, books_review.created_at AS 'created_at' FROM books_book JOIN books_review ON books_book.id = books_review.book_id JOIN books_user ON books_user.id = books_review.user_id WHERE books_book.id = {} ORDER BY books_review.created_at ASC".format(book_id))
		return book_data
	def home_data(self):
		recent_review = Book.objects.raw("SELECT books_book.id, books_review.rating, books_user.id AS 'user_id', books_user.alias, books_review.description, books_review.created_at AS 'created_at' FROM books_book JOIN books_review ON books_review.book_id = books_book.id JOIN books_user ON books_review.user_id = books_user.id ORDER BY books_review.created_at DESC LIMIT 3")
		books = Book.objects.all()
		return (recent_review, books)


class User(models.Model):
	name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100)
	email = models.EmailField()
	hashed_pw = models.CharField(max_length=255) # hashed password
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = UserManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
	# *************************

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	bookManager = bookManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()

class Review(models.Model):
	rating = models.IntegerField()
	description = models.TextField(max_length=500)
	user = models.ForeignKey(User)
	book = models.ForeignKey(Book)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	reviewManager = reviewManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
