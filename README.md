python-angellist
================

Python library for interacting with the Angel.co API

Usage: Create a Angellist object by passing a valid access_token, please note that GET requests do not need access_token to be provided.

API Reference URL: https://api.angel.co/1/

Usage:

from angellist import AngelList 

access_token = 'GIVE YOUR ACCESS TOKEN HERE'

angelapi = AngelList(access_token)


Eg 1: To use Search API:

angelapi.search({'method':'GET', 'query':'search-string'})


Eg 2: To get details about logged in user:

angelapi.me({'method':'POST'})


Eg 3: To get details about a particular startup, the 'id' needs to be passed on

angelapi.startups({'method':'GET', 'id':'123'})


To use API with _ (underscore in their name) like status_updates, startup_roles etc an additional _ needs to be passed on

Eg 4: To delete a particular status update with its id

angelapi.status__updates({'method':'DELETE', 'id':'123'})

Please note that status__updates in API doc is replaced as status__updates


Eg 5: To get startup roles

angelapi.startup__roles({'method':'GET', 'v':'1'})
