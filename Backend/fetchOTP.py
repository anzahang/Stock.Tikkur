import base64
import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Authentication function
def authenticate(email,password):
    # Set up the OAuth 2.0 credentials using the Gmail API
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    # The file token.json stores the user's access and refresh tokens.
    token_path = 'token.json'

    # Try to load the existing credentials
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If there are no valid credentials, prompt the user to authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    # Build the Gmail API service
    service = build('gmail', 'v1', credentials=creds)
    return service


# Function to find an email by subject
def findEmail(service, subject):
    try:
        # Search for emails with the specified subject
        results = service.users().messages().list(userId='me', q=f'subject:{subject}').execute()
        messages = results.get('messages', [])

        if not messages:
            return None  # No email found with the given subject

        # Get the first message
        email_id = messages[0]['id']
        message = service.users().messages().get(userId='me', id=email_id).execute()
        return message

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Function to get OTP from an email
def getOTP(email):
    if email is not None:
        try:
            otp = ""
            # Find otp in email
            return otp
        except Exception as e:
            print(f"Failed to extract OTP: {e}")

    return None
