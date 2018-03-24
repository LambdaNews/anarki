
import pdb
import google
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

import os
import base64
data = os.environ['FIREBASE_KEY']
key = base64.b64decode(data)
with open('firebase-service-account.json', 'w') as f:
    f.write(key)

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file(
    "./firebase-service-account.json", scopes=scopes)

# # Use the credentials object to authenticate a Requests session.
authed_session = AuthorizedSession(credentials, refresh_timeout=31536000000)
# response = authed_session.get(
#     "https://lambda-news.firebaseio.com/users/ada/name.json")

# Or, use the token directly, as described in the "Authenticate with an
# access token" section below. (not recommended)
request = google.auth.transport.requests.Request(session=authed_session)
credentials.refresh(request)
access_token = credentials.token
print(access_token)

os.remove('./firebase-service-account.json')
