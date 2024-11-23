from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

@login_required
def MyAccountView(request):
	return render(request, 'myaccount.html')

def SignUpView(request):

	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if form.is_valid():
			user = form.save()

			login(request, user)
			return redirect('core:frontpage')
	else:
		form = SignUpForm()

	return render(request, "signup.html", context = { "form": form })