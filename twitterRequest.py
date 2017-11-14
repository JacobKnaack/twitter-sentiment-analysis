import json
import collections
import urllib
import requests
import random
import base64
import binascii
import hmac
import hashlib
import time
from requests_oauthlib import OAuth1

API_CONFIG = json.load(open('./.config.json'))

def escape(s):
    return urllib.parse.quote(s, safe='~')

def generate_nonce():
    #generates a unique token for each API request
    return ''.join([str(random.randint(0,9)) for i in range(24)])


def generate_signature(method, url, url_parameters, oauth_parameters, oauth_consumer_key, oauth_consumer_secret, oauth_token_secret=None, status=None):
    temp = collect_parameters(oauth_parameters, status, url_parameters)

    parameter_string = stringify_parameters(temp)

    signature_base_string = (
        method.upper() + '&' +
        escape(str(url)) + '&' +
        escape(parameter_string)
    ).encode('utf-8')

    signing_key = create_signing_key(oauth_consumer_secret, oauth_token_secret)
    return calculate_signature(signing_key, signature_base_string)


def collect_parameters(oauth_parameter, status, url_parameters):
    temp = oauth_parameters.copy()
    if status is not None:
        temp['status'] = status

    for k, v, in url_parameters.items():
        temp[k] = v

    return temp


def stringify_parameters(parameters):
    output = ''
    ordered_parameters = {}
    ordered_parameters = collections.OrderedDict(sorted(parameters.items()))

    counter = 1
    for k, v in ordered_parameters.items():
        output += escape(str(k)) + '=' + escape(str(v))
        if counter < len(ordered_parameters):
            output += '&'
            counter += 1

    return output


def create_signing_key(oauth_consumer_secret, oauth_token_secret=None):
    signing_key = escape(oauth_consumer_secret) + '&'

    if oauth_token_secret is not None:
        signing_key += escape(oauth_token_secret)

    return signing_key.encode()


def calculate_signature(signing_key, signature_base_string):
    hashed = hmac.new(signing_key, signature_base_string, hashlib.sha1)

    sig = binascii.b2a_base64(hashed.digest())[:-1]

    return escape(sig)


AUTH_URL = 'https://api.twitter.com/1.1/account/verify_credentials.json'
FETCH_URL = 'https://api/twitter.com/1.1/search'
AUTH_PARAMS = {}
FETCH_PARAMS = {}

METHOD = 'get'
API_KEY = API_CONFIG["API_KEY"]
API_SECRET = API_CONFIG["API_SECRET"]
ACCESS_TOKEN = API_CONFIG["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = API_CONFIG["ACCESS_TOKEN_SECRET"]
OAUTH_TIMESTAMP = str(int(time.time()))
OAUTH_SIGNATURE_METHOD = 'HMAC-SHA1'
OAUTH_VERSION = '1.0'
OAUTH_NONCE = generate_nonce()

oauth_parameters = {
    'oauth_timestamp': OAUTH_TIMESTAMP,
    'oauth_signature_method': OAUTH_SIGNATURE_METHOD,
    'oauth_version': OAUTH_VERSION,
    'oauth_token': ACCESS_TOKEN,
    'oauth_nonce': OAUTH_NONCE,
    'oauth_consumer_key': API_KEY
}

oauth_parameters['oauth_signature'] = generate_signature(
    METHOD,
    AUTH_URL,
    AUTH_PARAMS, oauth_parameters,
    API_KEY,
    API_SECRET,
    ACCESS_TOKEN_SECRET
)

AUTH = OAuth1(oauth_parameters)
authRequest = requests.get(AUTH_URL, auth=AUTH)
#fetchRequest = requests.get(url = URL, params = PARAMS)

if authRequest.status_code == 200:
    print ('success:', authRequest.json())
else:
    print ('request failed: ', authRequest.json())

#data = request.json()

#print("twitter response: ", data)
