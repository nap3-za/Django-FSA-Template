from django.conf import settings
from django.utils import timezone
from .utils import field_choices_to_list


def presence_validator(data):
	if (data == None) or (type(data) == str and data.replace(" ","") == ""):
		return False

	return True

def choice_validator(selected, choices):
	if presence_validator(selected):
		# First condition is for cases where choices is not a nested set
		if (not selected in choices) and (not selected in field_choices_to_list(choices)):
			return f"{selected} is not a valid choice."
	else:
		return False
	
	return True

def past_date_validator(date):
	if presence_validator(date):
		if date > timezone.now().date():
			return f"date cannot be a future date"
	else:
		return False

	return True

def future_date_validator(date):
	if presence_validator(date):
		if date < timezone.now().date():
			return f"date cannot be a past date"
	else:
		return False

	return True

def size_validator(integer, min_size=None, max_size=None):
	if presence_validator(integer):
		if min_size and integer <= min_size:
			return f"{integer} is below {min_size}"

		if max_size and integer >= max_size:
			return f"{integer} is above {max_size}"
	else:
		return False

	return True

def length_validator(text, min_len):
	if presence_validator(text):
		if len(text) < min_len:
			return "length is too small"
	else:
		return False

	return True 



