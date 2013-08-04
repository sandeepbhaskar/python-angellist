# -*- coding: utf-8 -*-

from urllib import urlencode
import urllib2
import json

ANGELLIST_API_URL = "https://api.angel.co/1/"

class AngelList(object):
	
	def _request(self, endpoint, data, method="POST"):
		if method in ["GET"]:
			return json.loads(urllib2.urlopen("%s%s?%s" % (ANGELLIST_API_URL, endpoint, urlencode(data))).read())
		if not self.access_token:
			return {'error':'No access token'}
		return json.loads(urllib2.urlopen("%s%s?access_token=%s&%s" % (ANGELLIST_API_URL, endpoint, self.access_token, urlencode(data))).read())

	def __init__(self, access_token = None):
		self.access_token	= access_token

	def __getattr__(self, name):
		def wrapper(data):
			if 'method' in data:
				method = data['method'] 
				del data['method']
			else:
				method = "POST"

			response = self._request(name, data, method)
			return response
		return wrapper