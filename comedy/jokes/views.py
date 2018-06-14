from django.shortcuts import render, render_to_response

def home(request, template_name="home.html"):
	context = {'title': 'Jokes Central'}
	return render_to_response(template_name, context)
