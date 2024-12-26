
def field_choices_to_list(data_tuple=None):
	if data_tuple:
		data_list = []
		for item in data_tuple:
			data_list.append(item[0])
		return data_list