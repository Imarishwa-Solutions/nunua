import os
from django.conf import settings

#from duka.logicController import *
from duka.contentController import *

import json
import requests

PAGE_ACCESS_TOKEN = settings.PAGE_ACCESS_TOKEN
VERIFY_TOKEN = settings.VERIFY_TOKEN


post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN

class FBMessageAPI:
	"""docstring for FBMessageAPI"""
	def __init__(self, fb_id):
		self.fb_id = fb_id

	def text_message(self, content):
		response_msg = json.dumps({
			"recipient": {
				"id": self.fb_id}, 
			"message": {
				"text": content}})
		requests.post(post_message_url, headers={
			"Content-Type": "application/json"
			}, 
			data=response_msg)

	def image_message(self, image):
		response_img = json.dumps({
			"recipient": {
					"id": self.fb_id},
					"message": {
							"attachment": {
									"type": "image",
									"payload": {
											"url": image}
											}
											}
											})
		requests.post(post_message_url, headers={
			"Content-Type": "application/json"
			}, 
			data=response_img)

	def template_message(self, title, image_url, subtitle, data):
		response_template = json.dumps({
			"recipient": {
					"id": self.fb_id}, 
					"message": {
							"attachment": {
									"type": "template",
									"payload": {
											"template_type": "generic",
											"elements": [{
													"title": title,
													"image_url": image_url,
													"subtitle": subtitle,
													"buttons": data
													}]
												}
											}}})
		requests.post(post_message_url, headers={
			"Content-Type": "application/json"
			}, 
			data=response_template)

	def quick_reply_message(self, text, quick_replies):
		response_fast = json.dumps({
			"recipient":{
				"id":self.fb_id,
			},
			"message":{
				"text":text,
				"quick_replies":quick_replies
			}
			})
		requests.post(post_message_url, headers = {
			"Content-Type": "application/json"
			}, 
			data = response_fast)