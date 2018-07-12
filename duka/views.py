import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import generic


from duka.messenger_api import *
from duka.logicController import *
from duka.contentController import *

import json
from pprint import pprint

PAGE_ACCESS_TOKEN = settings.PAGE_ACCESS_TOKEN
VERIFY_TOKEN = settings.VERIFY_TOKEN
'''
def post_facebook_message(fbid, recevied_message):
	user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
	user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
	user_details = requests.get(user_details_url, user_details_params).json()
	
	fb = FBMessageAPI(fb_id)

	if recevied_message == "hi":
		content = Hello()
		fb.text_message(content)
		return 0
'''

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
