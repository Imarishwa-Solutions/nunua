import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json
import logging
from pprint import pprint

# Create your views here.
logger = logging.getLogger(__name__)

VERIFY_TOKEN      = '12345'
PAGE_ACCESS_TOKEN = 'EAAIAJa4N4gUBAMaTBSnSeHZAhOpERjItaUZBJfGLZCEiKLwuV40wiRCFGfETQyaPB4W1JP357paTs6sHmvEepIsWzCM9lywC4QnJnZBduA6L6oZCsCguY0ZBDuWWm0mfCd6phVCNR4fbQwABVLlsJnqgr8uDkkHAu5tkiDTtcgkQZDZD'

class Webhook(View):
	#docstring for Verification
	def get(self, request):
		if request.method  == 'GET':
			if request.GET['hub.verify_token'] == VERIFY_TOKEN:
				return HttpResponse(request.GET['hub.challenge'],status= 200)
			else:
				return HttpResponse("Error,invalid token")




