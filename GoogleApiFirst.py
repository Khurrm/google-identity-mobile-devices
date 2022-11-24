from google.oauth2 import service_account
import googleapiclient.discovery
import json
import pprint
from six.moves import urllib
import google.auth.transport.requests
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/cloud-identity.devices']
SERVICE_ACCOUNT_FILE = '/path/to/service-account-file.json'

def create_service():
  credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
  delegated_credentials = credentials.with_subject('mail@XXXX.com')

  return service


