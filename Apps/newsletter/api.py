from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Subscriber
import json


def api_add_subscriber(request):
	data = json.loads(request.body)
	email = data.get('email')
	

	if len(email) == 0 or len(Subscriber.objects.filter(email=email)):
		return JsonResponse({"error": True})
	
	Subscriber.objects.create(email=email)

	return JsonResponse({ "success": True })