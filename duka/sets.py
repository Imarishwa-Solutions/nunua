import os
from django.conf import settings
import requests
import json

PAGE_ACCESS_TOKEN = "EAADqWBHjJygBAG8xsjYOh7Y2ut7x5eGyEkOdMbAmoJfuaiY8Olva3vaPP7HzqXSDfOyrwml3n16J6Mulc5TposhsExl2FltB3oXFdyJGzi6ZA08CxVQ9mDuCLVq8bVfROhZAGohXyK0fgQ2b85ZBdUEU4knnnEZB5OVOwcaBQwZDZD"
messenger_profile = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=%s" % PAGE_ACCESS_TOKEN

def get_started():
	payload = json.dumps({
		"get_started":{
				"payload":"Get Started"
		}
		})
	return requests.post(messenger_profile, headers ={
				"Content-Type": "application/json"},
				data = payload)