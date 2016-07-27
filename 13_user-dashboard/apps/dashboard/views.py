from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, Message, Post
# Create your views here.
def index(request):
	return render(request, 'dashboard/index.html')

def register_page(request):
	return render(request, 'dashboard/register_page.html')

def process_user(request, process):
	if request.method == "POST":
		if process == "register":
			val_result = User.userManager.register(request.POST)
			if val_result[0] == False: # aka registration info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect(reverse('register'))
			else: # registration info is VALID (therefore, Successfully registered!)
				messages.success(request, val_result[1])
				request.session['user_id'] = val_result[2]
				request.session['status'] = True
				return redirect('/home')
		else: # case when 'which_process' == "login"
			val_result = User.userManager.login(request.POST)
			if val_result[0] == False: # aka login info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect(reverse('index'))
			else: # login info is VALID (therefore, Successfully logged in!)
				messages.success(request, val_result[1])
				request.session['user_id'] = val_result[2] # user id!
				request.session['status'] = True
				return redirect('/home')
	else:
		messages.error(request, "This is POST route so don't do that!")
		return redirect('/')

def logout(request):
	if 'status' in request.session:
		request.session.flush()
		messages.success(request, "Successfully log off!")
		return redirect('/')
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def success(request):
	if 'status' in request.session:
		user = User.objects.get(id=request.session['user_id'])
		context = {
			'user': user
		}
		return render(request, 'dashboard/home.html',context)
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def manage_users(request, user_level):
	if 'status' in request.session:
		users = User.objects.all()
		context = {
			'users': users,
			'user_level': user_level
		}
		return render(request, 'dashboard/manage_users.html', context)
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def new_user(request):
	if 'status' in request.session:
		if request.method == "GET":
			return render(request, 'dashboard/new.html')
		elif request.method == "POST":
			val_result = User.userManager.register(request.POST)
			if val_result[0] == False: # aka registration info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect('/users/new')
			else: # registration info is VALID (therefore, Successfully registered!)
				messages.success(request, val_result[1])
				return redirect('/manage/admin')
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def delete_user(request, user_id):
	if 'status' in request.session:
		if request.method == "GET":
			context = {
				'user': User.objects.get(id=user_id)
			}
			return render(request, 'dashboard/delete.html' ,context)
		elif request.method == "POST":
			User.objects.get(id=user_id).delete()
			messages.success(request, "Successfully deleted a user!")
			return redirect('/manage/admin')
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def profile_edit(request):
	if 'status' in request.session:
		if request.method == "GET":
			context = {
				'user': User.objects.get(id=request.session['user_id'])
			}
			return render(request, 'dashboard/my_profile.html', context)
		if request.method == "POST":
			if request.POST['which_update'] == "email_name":
				val_result = User.userManager.email_name_update(request.POST, request.session['user_id'])
			elif request.POST['which_update'] == "password":
				val_result = User.userManager.password_update(request.POST, request.session['user_id'])
			elif request.POST['which_update'] == "description":
				val_result = User.userManager.description_update(request.POST, request.session['user_id'])

			if val_result[0] == False:
				for error in val_result[1]:
					messages.error(request, error)
				return redirect('/users/edit')
			else:
				messages.success(request, val_result[1])
				return redirect('/users/edit')
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def edit_user_by_admin(request, user_id):
	if 'status' in request.session:
		if request.method == "GET":
			context = {
				'user': User.objects.get(id=user_id)
			}
			return render(request, 'dashboard/edit_user_by_admin.html', context)
		elif request.method == "POST":
			if request.POST['which_update'] == "user_total":
				val_result = User.userManager.user_total_update(request.POST, user_id)
			elif request.POST['which_update'] == "password":
				val_result = User.userManager.password_update(request.POST, user_id)

			if val_result[0] == False:
				for error in val_result[1]:
					messages.error(request, error)
				return redirect('/users/edit/{}'.format(user_id))
			else:
				messages.success(request, val_result[1])
				return redirect('/users/edit/{}'.format(user_id))
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def user_wall(request, user_id):
	if 'status' in request.session:
		data = Message.messageManager.retrieve_message(user_id)
		posts = Post.postManager.retrieve_post(user_id)
		context = {
			'user': data[0],
			'message_list': data[1],
			'posts': posts
		}
		return render(request, 'dashboard/user_wall.html', context)
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def add_message(request, to_who):
	if 'status' in request.session:
		if request.method == "POST":
			val_result = Message.messageManager.add_message(request.POST['message'], to_who, request.session['user_id'])
			if val_result[0] == False:
				messages.error(request, val_result[1])
			else:
				messages.success(request, val_result[1])
			return redirect('/users/show/{}'.format(to_who))
		else:
			# do nothing
			return redirect('/users/show/{}'.format(to_who))
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def add_message(request, to_who):
	if 'status' in request.session:
		if request.method == "POST":
			val_result = Message.messageManager.add_message(request.POST['message'], to_who, request.session['user_id'])
			if val_result[0] == False:
				messages.error(request, val_result[1])
			else:
				messages.success(request, val_result[1])
			return redirect('/users/show/{}'.format(to_who))
		else:
			# do nothing
			return redirect('/users/show/{}'.format(to_who))
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def add_post(request, message_id, user_id):
	if 'status' in request.session:
		if request.method == "POST":
			val_result = Post.postManager.add_post(request.POST['post'], message_id, request.session['user_id'])
			if val_result[0] == False:
				messages.error(request, val_result[1])
			else:
				messages.success(request, val_result[1])
			return redirect('/users/show/{}'.format(user_id))
		else:
			# do nothing
			return redirect('/users/show/{}'.format(user_id))
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')
