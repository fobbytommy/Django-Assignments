from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	# User.objects.all().delete()
	request.session.flush()
	return render(request, 'loginReg/index.html')

def process(request, which_process):
	if request.method == "POST":
		if which_process == "register":
			val_result = User.userManager.register(request.POST)
			if val_result[0] == False: # aka registration info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect(reverse('loginReg_index'))
			else: # registration info is VALID (therefore, Successfully registered!)
				request.session['name'] = request.POST['first_name']
				messages.success(request, val_result[1])
				return redirect(reverse('loginReg_success'))
		else: # case when 'which_process' == "login"
			val_result = User.userManager.login(request.POST)
			if val_result[0] == False: # aka login info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect(reverse('loginReg_index'))
			else: # login info is VALID (therefore, Successfully logged in!)
				messages.success(request, val_result[1])
				request.session['name'] = val_result[2] # first_name
				return redirect(reverse('loginReg_success'))
	else:
		return redirect(reverse('loginReg_index'))

def success(request):
	return redirect('/courses/courses/add_user')
