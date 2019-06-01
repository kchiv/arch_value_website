from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def hp_contact_form(request):
	if request.method == 'POST':
		user_type = request.POST['user_type']
		name = request.POST['user_name']
		email = request.POST['user_email']
		phone_number = request.POST['user_phone']
		company_name = request.POST['user_company']
		message = request.POST['user_message']
		if 'user_subscribe' in request.POST:
			subscriber = True
		else:
			subscriber = False

		# error_template = 'The {} entered must be less than {} characters.'

		# if len(name) > 50:
		# 	error_message = error_template.format('name', '50')
		# 	return redirect('home')
		# else:
		# 	if len(email) > 254:
		# 		error_message = error_template.format('email', '254')
		# 	else:
		# 		if len(phone_number) > 50:
		# 			error_message = error_template.format('phone number', '50')
		# 		else:
		# 			if len(company_name) > 100:
		# 				error_message = error_template.format('company name', '100')
		# 			else:
		# 				if len(message) > 1000:
		# 					error_message = error_template.format('message', '1,000')
		# 				else:
		contact = Contact(user_type = user_type,
							name = name,
							email = email,
							phone_number = phone_number,
							company_name = company_name,
							message = message,
							subscriber = subscriber)

		contact.save()
		return redirect('home')