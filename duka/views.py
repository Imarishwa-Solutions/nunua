import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import generic



from duka.messengerAPI import *

import json
from pprint import pprint

VERIFY_TOKEN = settings.VERIFY_TOKEN
PAGE_ACCESS_TOKEN = settings.PAGE_ACCESS_TOKEN


def post_facebook_message(fb_id, recieved_message):
	fb = FBMessageAPI(fb_id)

	if recieved_message == "Get Started":
		content = GetStarted()
		fb.text_message(content)
		return 0
	elif recieved_message == "Mpesa":
		content = Mpesa()
		fb.text_message(content)
		return 0
	else:
		content = Human()
		fb.text_message(content)
		return 0



class Webhook(generic.View):
	#docstring for Verification

	def get(self, request):
		if request.method  == 'GET':
			if request.GET['hub.verify_token'] == VERIFY_TOKEN:
				return HttpResponse(request.GET['hub.challenge'],status= 200)
			else:
				return HttpResponse("Error,invalid token")

	@method_decorator(csrf_exempt)
	def dispatch(self, request,*args, **kwargs):
		return generic.View.dispatch(self,request,*args,**kwargs)

	def post(self, request,*args, **kwargs):
		incoming_message = json.loads(self.request.body.decode('utf-8'))
		pprint(incoming_message)
		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				if 'message' in message:
					pprint(message)
					#print('message')
					try:
						post_facebook_message(message['sender']['id'],message['message']['text'])
					except:
						return HttpResponse()
				if 'postback' in message:
					pprint(postback)
					#print('postback')
					try:
						post_facebook_message(message['sender']['id'],message['postback']['payload'])
					except:
						return HttpResponse()
		return HttpResponse()
