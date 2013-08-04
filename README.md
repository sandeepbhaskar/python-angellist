python-angellist
================

Python library for interacting with the Angel.co API

Usage: Create a Angellist object, passing either the api key or your username and password as the parameters

https://api.angel.co/1/

To User
from angellist import AngelList

#access_token is not required for GET requests

access_token = 'GIVE YOUR ACCESS TOKEN HERE'
angelapi = AngelList(access_token)

#Eg 1: To use Search API:
angelapi.search({'method':'GET', 'query':'search-string'})

#Eg 2: To get details about logged in user:

angelapi.me({'method':'POST'})
