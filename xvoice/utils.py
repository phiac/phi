# utils.py
from twilio.rest import Client

def send_sms(phone_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_='your_twilio_number',
        to=phone_number
    )
    return message.sid

def generate_otp():
    import random
    return str(random.randint(100000, 999999))

def verify_otp(otp, user_otp):  # user_otp is the OTP stored for the user
    return otp == user_otp
