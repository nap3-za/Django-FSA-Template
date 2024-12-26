from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import (
	SignUpForm,
	SignInForm,
	UpdateAccountForm,
	DeleteAccountForm,
)

from .models import Account


def sign_up_view(request, *args, **kwargs):
	context = {
		"form": SignUpForm()
	}

	if request.user.is_authenticated:
		return redirect("dashboard")
	elif request.method == "POST" and request.POST:
		form = SignUpForm(request.POST)
		if form.is_valid():
			auth_user_account = form.save()
			login(request, auth_user_account)
			return redirect("dashboard")
		else:
			context["form"] = form
	else:
		pass

	return render(request, 'account/sign-up.html', context)


def sign_in_view(request, *args, **kwargs):
	context = {
		"form": SignInForm()
	}

	if request.user.is_authenticated:
		return redirect("dashboard")
	elif request.method == 'POST' and request.POST:
		form = SignInForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			try:
				auth_user_account = authenticate(username=username, password=password)
				if auth_user_account != None:
					login(request, auth_user_account)
					return HttpResponse("-", headers={"HX-Redirect":reverse("dashboard")})
			except:
				pass

		context["form"] = form

	if request.htmx:
		return render(request, "account/htmx-partials/sign-in-form.html", context)

	return render(request, "account/sign-in.html", context)


# @login_required(login_url="sign-in")
def logout_view(request):
	logout(request)
	return redirect("sign-in")


@login_required(login_url="sign-in")
def delete_account_view(request, *args, **kwargs):
	auth_user_account = get_object_or_404(Account, id=request.user.id)
	context = {
		"form": DeleteAccountForm()
	}

	if request.method == "POST" and request.POST:
		form = DeleteAccountForm(request.POST)
		if form.is_valid():
			form.save(instance=auth_user_account)
			return redirect("sign-up")

		context["form"] = form
	else:
		pass

	return render(request, "account/delete-account.html", context)


@login_required(login_url="sign-in")
def details_view(request, *args, **kwargs):
	context = {}

	subject_account = None
	try:
		auth_user_account = Account.objects.get(id=request.user.id)
		if kwargs.get("subject_username") != auth_user_account.username:
			subject_account = Account.objects.get(username=kwargs.get("subject_username"))
		else:
			subject_account = auth_user_account
	except:
		return redirect("404")
	
	context["subject"] = subject_account

	is_self = False
	if auth_user_account == subject_account:
		is_self = True
		context["form"] = UpdateAccountForm(instance=auth_user_account)

	if request.method == "POST" and request.POST:
		form = UpdateAccountForm(request.POST, request.FILES, instance=auth_user_account)
		print(request.FILES)
		if form.is_valid():
			updated_auth_user_account = form.save()
			context["message"] = "Account updated successfully"
			context["subject"] = updated_auth_user_account
			context["form"] = UpdateAccountForm(instance=updated_auth_user_account)
			if kwargs.get("subject_username") != updated_auth_user_account.username:
				context["new_username"] = True # used to change username in browser url
		else:
			context["form"] = form

	if request.htmx:
		return render(request, "account/htmx-partials/update-form.html", context)
	
	context['is_self'] = is_self
	return render(request, "account/details.html", context)
