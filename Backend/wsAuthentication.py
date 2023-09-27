from fetchOTP import *
from wsimple.api import Wsimple

def getOTP():
    email_service = authenticate('your_email@gmail.com', 'your_password')
    subject_to_search = 'Your Subject'
    email = findEmail(email_service, subject_to_search)

    if email:
        otp = getOTP(email)
        print(f"OTP found: {otp}")
    else:
        print("Email not found.")

def wsAuthenticate(email,password,otp):
    ws = Wsimple(email, password, otp)

    # always check if wealthsimple is working (return True if working or an error)
    if ws.is_operational():
        print(ws.get_activities)

    #Do something

# Get as many of these as needed
def getData():
    pass

def passToFrontend():
    pass