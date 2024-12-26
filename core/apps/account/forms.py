from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit, HTML, Div

from .models import Account


class SignUpForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column("name", css_class="form-group col-sm-6"),
				Column("surname", css_class="form-group col-sm-6"),
			),
			
			"gender",
			Row(
				Column("email", css_class="form-group col-sm-6"),
				Column("phone_number", css_class="form-group col-sm-6"),
			),
			"username",
			Row(
				Column("password1", css_class="form-group col-sm-6"),
				Column("password2", css_class="form-group col-sm-6"),
			),
			"accept",
			Submit("submit", "Sign up", css_class="btn btn-primary btn-block")
		)


	class Meta:
		model = Account
		fields = (
			"username",
			"name",
			"surname",
			"gender",
			"password1",
			"password2",

			"email",
			"phone_number",

			"accept",
		)

	def clean_accept(self):
		accept = self.cleaned_data["accept"]
		if not accept:
			raise forms.ValidationError(f"You must accept the privacy policy and terms of use to continue")
		return accept

	
class SignInForm(forms.ModelForm):
	password 								= forms.CharField(label="Password", widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(SignInForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout()
		for field_name, field in self.fields.items():
			self.helper.layout.append(
				Field(field_name, placeholder=field.label)
		)
		self.helper.layout.append(
			Submit("submit", "Sign in", css_class="btn btn-primary btn-block")
		)
		self.helper.form_show_errors = False
		self.helper.form_show_labels = False

	class Meta:
		model = Account
		fields = ("username", "password")

	def clean(self):
		username = self.cleaned_data["username"]
		password = self.cleaned_data["password"]
		try:
			account = Account.objects.get(username=username)
			auth_user_account = authenticate(username=username, password=password)
			if auth_user_account == None:
				raise forms.ValidationError("Invalid login")
		except:
			raise forms.ValidationError("Invalid login")


class UpdateAccountForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(UpdateAccountForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Div(
					HTML("""
						<img src='{{ request.user.profile_image.url }}' class='profile-image img-fluid pb-4' alt='profile-image'>
					"""),
					"profile_image",
					css_class="col-lg-4",
				),

				Div(
					"username",
					Row(
						Column("name", css_class="form-group col-sm-6"),
						Column("surname", css_class="form-group col-sm-6"),
					),
					
					"gender",
					Row(
						Column("email", css_class="form-group col-sm-6"),
						Column("phone_number", css_class="form-group col-sm-6"),
					),
					Submit("submit", "Update account", css_class="btn btn-outline-primary bg-white"),
					css_class="col-lg-6"
				),
				css_class="form-row align-items-center justify-content-around"
			)
		)

	class Meta:
		model = Account
		fields = (
			"username",
			"name",
			"surname",
			"gender",
			"profile_image",

			"email",
			"phone_number",
		)


class DeleteAccountForm(forms.Form):
	username 					= forms.CharField(label="Username", max_length=250, required=True)
	password 					= forms.CharField(label="Password", widget=forms.PasswordInput)


	def __init__(self, *args, **kwargs):
		super(DeleteAccountForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout()
		for field_name, field in self.fields.items():
			self.helper.layout.append(
				Field(field_name, placeholder=field.label)
		)
		self.helper.layout.append(
			Submit("submit", "Delete Account", css_class="btn btn-danger btn-block")
		)
		self.helper.form_show_errors = False
		self.helper.form_show_labels = False

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data["password"]
		try:
			auth_user_account = authenticate(username=username, password=password)
			if auth_user_account != None:
				return self.cleaned_data
			else:
				raise forms.ValidationError("Invalid login")
		except:
			raise forms.ValidationError("Invalid login")

	def save(self, instance):
		instance.delete()
