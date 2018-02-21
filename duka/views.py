import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json
import logging
from pprint import pprint



VERIFY_TOKEN      = '12345'
PAGE_ACCESS_TOKEN = 'EAACGMh4sRe0BAEZAh57D0z7verY4TcLvk6LFnIZCfECMDzfvF4BT4NBWMLxMolPsGAVNyF2wdgHf5MGAo0SjkgHJ5yqLL0LILd1pyewIsB4ucNqcJkeb8wnYvBY7MGFjXYO7gWoFWip65aSCqz1E69F2Xc0rXdMr8HB7aZBpAZDZD'

class Webhook(View):
	#docstring for Verification
	def get(self, request):
		if request.method  == 'GET':
			if request.GET['hub.verify_token'] == VERIFY_TOKEN:
				return HttpResponse(request.GET['hub.challenge'],status= 200)
			else:
				return HttpResponse("Error,invalid token")




