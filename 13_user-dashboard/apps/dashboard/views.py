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
