import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
import logging
from pprint import pprint



VERIFY_TOKEN      = '12345'
PAGE_ACCESS_TOKEN = 'EAACGMh4sRe0BAP6a06vc7ZAbllvoUgRqt7H3GDS3I9ryxLbWAcT1AKBje0RZCTeBbXfcNTcdBMlQ2dkRBFZBcAKSfm5ybSh15tNSmItMdzPWjjB01OvtRQW5icjhDjwUcKLlhgukTVzaJkHQWrXzNyjoKoWEJbGz7rd0aM4KwZDZD'

class Webhook(View):
	#docstring for Verification
	def get(self, request):
		if request.method  == 'GET':
			if request.GET['hub.verify_token'] == VERIFY_TOKEN:
				return HttpResponse(request.GET['hub.challenge'],status= 200)
			else:
				return HttpResponse("Error,invalid token")





