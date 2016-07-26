from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, Book, Review
# Create your views here.


def index(request):
	return render(request, 'books/index.html')


def process_user(request, process):
	if request.method == "POST":
		if process == "register":
			val_result = User.userManager.register(request.POST)
			if val_result[0] == False: # aka registration info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect(reverse('index'))
			else: # registration info is VALID (therefore, Successfully registered!)
				request.session['alias'] = request.POST['alias']
				messages.success(request, val_result[1])
				request.session['status'] = True
				return redirect(reverse('show_books'))
		else: # case when 'which_process' == "login"
			val_result = User.userManager.login(request.POST)
			if val_result[0] == False: # aka login info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect(reverse('index'))
			else: # login info is VALID (therefore, Successfully logged in!)
				messages.success(request, val_result[1])
				request.session['alias'] = val_result[2] # user alias!
				request.session['user_id'] = val_result[3] # user id!
				request.session['status'] = True
				return redirect(reverse('show_books'))
	else:
		return redirect(reverse('index'))


def show_books(request):
	if ('status' in request.session):
		data = Book.bookManager.home_data()
		context = {
			'recent_review': data[0],
			'books': data[1]
		}
		return render(request, 'books/books.html', context)
	else:
		messages.error(request, "Please login or register to go to that route!")
		return redirect(reverse('index'))


def logout(request):
	if ('status' in request.session):
		request.session.flush()
		messages.success(request, "Successfully logged out!")
	else:
		messages.error(request, "Cannot logout when you are not even logged in!")
	return redirect(reverse('index'))


def add_books(request):
	if ('status' in request.session):
		if request.method == "GET":
			context = {
				'authors': Book.objects.raw("SELECT books_book.author, books_book.id FROM books_book GROUP BY books_book.author")
			}
			return render(request, 'books/add_books.html', context)
		elif request.method == "POST":
			val_result = Book.bookManager.new_book(request.POST, request.session['user_id'])
			if val_result[0] == False: # aka book info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect('/books/add')
			else: # book info is VALID (therefore, Successfully added a book!)
				messages.success(request, val_result[1])
				return redirect('/books/{}'.format(val_result[2]))
	else:
		messages.error(request, "Please login or register to go to that route!")
		return redirect(reverse('index'))


def show_review(request, book_id):
	if ('status' in request.session):
		context = {
			'book_data': Book.bookManager.getting_info(book_id)
		}
		return render(request, 'books/show_review.html', context)
	else:
		messages.error(request, "Please login or register to go to that route!")
		return redirect(reverse('index'))


def add_review(request, book_id, user_id):
	if ('status' in request.session):
		if request.method == "POST":
			val_result = Review.reviewManager.add_review(request.POST, book_id, user_id)
			if val_result[0] == False:
				for error in val_result[1]:
					messages.error(request, error)
				return redirect('/books/{}'.format(book_id))
			else:
				messages.success(request, val_result[1])
				return redirect('/books/{}'.format(book_id))
		else:
			return redirect('/books/{}'.format(book_id))
	else:
		messages.error(request, "Please login or register to go to that route!")
		return redirect(reverse('index'))


def delete_review(request, book_id, review_id):
	if ('status' in request.session):
		if request.method == "POST":
			Review.objects.get(id=review_id).delete()
			messages.success(request, "Successfully deleted your review!")
			return redirect('/books/{}'.format(book_id))
		else:
			return redirect('/books/{}'.format(book_id))
	else:
		messages.error(request, "Please login or register to go to that route!")
		return redirect(reverse('index'))


def get_user(request, user_id):
	if ('status' in request.session):
		data = User.userManager.user_info(user_id)
		context = {
			'user': data[0],
			'total_review': data[1],
			'books_review': data[2]
		}
		return render(request, 'books/user_info.html', context)
	else:
		messages.error(request, "Please login or register to go to that route!")
		return redirect(reverse('index'))
