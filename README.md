# Django-Platform-Restriction

This is a simple decorator used to restrict access to a specific view using the user agent.

You can specify the user agents

	@require_platform(['iPhone'], redirect_to = "example.views.not_allowed_home")
	def view(request):
	    return HttpResponse("You are allowed to see this page");


or create some macro
	
	#django_platform_restriction.py
	require_iOS = require_platform(['iPhone', 'iPad'])
	
	#in your views.py or where you want..
	@require_iOS
	def view(request):
	    return HttpResponse("You are allowed to see this page");	
	

The 'redirect_to' param is optional, the decorator raise a 404 error if not supplied
