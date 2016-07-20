from django.shortcuts import render, redirect
import random
from time import strftime, localtime

def index(request):
	if ('current_gold' in request.session) == False:
		request.session['current_gold'] = 0
	return render(request, 'gold/index.html')

def process(request, building):
	if request.method == "POST":
		if ('activities' in request.session) == False:
			request.session['activities'] = []

		if building == "farm":
			gold = random.randint(10, 20)
		elif building == "cave":
			gold = random.randint(5, 10)
		elif building == "house":
			gold = random.randint(2, 10)
		elif building == "casino":
			gold = random.randint(-50, 50)

		request.session['current_gold'] += gold
		current_time = strftime('(%Y/%m/%d %I:%M:%S %p)', localtime())
		if gold > 0:
			request.session['activities'].insert(0, ['Earned {} golds from the {}! {}'.format(gold, building,  current_time), 'green'])
		elif gold < 0:
			request.session['activities'].insert(0, ['Entered a casino and lost {} golds... Ouch.. {}'.format(abs(gold), current_time), 'red'])
		else:
			request.session['activities'].insert(0, ['Entered a casino and you EVEN out...phew {}'.format(current_time), 'blue'])
		return redirect('/')
	else:
		return redirect('/')

def reset(request):
	if request.method == "POST":
		try:
			del request.session['current_gold']
			del request.session['activities']
		except:
			pass
		return redirect('/')
	else:
		return redirect('/')
