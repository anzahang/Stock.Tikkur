from wsimple.api import Wsimple


def get_otp():
    return input("Enter otpnumber: \n>>>")


email = str(input("Enter email: \n>>>"))
password = str(input("Enter password: \n>>>"))

ws = Wsimple(email, password, otp_callback=get_otp)

# always check if wealthsimple is working (return True if working or an error)
if ws.is_operational():
    print(ws.get_activities)