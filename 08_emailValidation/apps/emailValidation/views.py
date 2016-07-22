from django.shortcuts import render, redirect
from .models import Email
# Create your views here.
def index(request):
	return render(request, 'emailValidation/index.html')

def process(request):
	if request.method == "POST":
		val_result = Email.userManager.email(request.POST['email'])
		if val_result[0] == False:
			request.session['error'] = val_result[1]
			return redirect('/')
		elif val_result[0] == True:
			Email.objects.create(email=request.POST['email'])
			request.session['message'] = val_result[1]
			return redirect('/success')
	else:
		return redirect('/')

def success(request):
	if request.method == "GET":
		context = {
			'emails': Email.objects.all()
		}
		return render(request, 'emailValidation/success.html', context)
	else: # if verb is POST, then reset and back to main!
		try:
			del request.session['error']
			del request.session['message']
		except:
			pass
		return redirect('/')

def delete(request, id):
	if request.method == "POST":
		email = Email.objects.get(id=id)
		request.session['message'] = "You have successfully deleted {}!".format(email.email)
		email.delete()
		return redirect('/success')
	else:
		return redirect('/success')
