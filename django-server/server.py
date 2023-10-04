# In your app's views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from wsimple.api import Wsimple
import re
from google.oauth2 import service_account
from googleapiclient.discovery import build
import base64

@csrf_exempt  # Disable CSRF protection for simplicity in this example
def receive_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Path to your OAuth2 credentials JSON file
CREDENTIALS_FILE = 'path/to/your/credentials.json'

# Regular expression pattern to match OTP (6 digits)
OTP_PATTERN = r'\b\d{6}\b'

otpFinal = ""
def get_latest_otp_from_email(service):
    # Search for emails with the specified subject, sorted by date in descending order (latest first)
    results = service.users().messages().list(userId='me', q='subject:	Wealthsimple verification code', orderBy='date desc').execute()
    messages = results.get('messages', [])

    if messages:
        latest_message = messages[0]  # Get the latest email
        msg = service.users().messages().get(userId='me', id=latest_message['id'], format='raw').execute()
        msg_raw = base64.urlsafe_b64decode(msg['raw'].encode('ASCII')).decode('utf-8')

        # Use regular expression to find OTP in the email content
        otp_matches = re.findall(OTP_PATTERN, msg_raw)

        if otp_matches:
            otpFinal = otp_matches[0]  # Return the first OTP found (if any)




def WS_Authentication(email,password,otp):
    pass

