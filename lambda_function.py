import json
import requests
import urllib.request
from requests.exceptions import HTTPError
import time
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    # TODO implement

    #url = 'http://facebook.com'
    url = 'https://animeflv.net'
    response = requests.get(url, json={'key': 'value'})
    response.encoding = 'utf-8'

    seach_key = 'title'
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.findAll(seach_key)

    return {
        'statusCode': response.status_code,
        'tags': tags
    }

print( lambda_handler('','') )