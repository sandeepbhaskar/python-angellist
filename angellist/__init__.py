# -*- coding: utf-8 -*-

from urllib import urlencode
import urllib2
import json

ANGELLIST_API_URL = "https://api.angel.co/1/"

class AngelList(object):
	
	def _request(self, endpoint, data, method="POST", _id=None):
		if method in ["GET"]:
			if _id:
				return json.loads(urllib2.urlopen("%s%s/%s?%s" % (ANGELLIST_API_URL, endpoint, _id, urlencode(data))).read())
			else:
				return json.loads(urllib2.urlopen("%s%s?%s" % (ANGELLIST_API_URL, endpoint, urlencode(data))).read())
		if not self.access_token:
			return {'error':'No access token'}
		return json.loads(urllib2.urlopen("%s%s?access_token=%s&%s" % (ANGELLIST_API_URL, endpoint, self.access_token, urlencode(data))).read())

	def __init__(self, access_token = None):
		self.access_token	= access_token

	def __getattr__(self, name):
		def wrapper(data):
			_id = None
			if 'method' in data:
				method = data['method'] 
				del data['method']
			else:
				method = "POST"
			if 'id' in data:
				_id=data['id']
				del data['id']
			return self._request(name.replace("__","/"), data, method, _id)
		return wrapper