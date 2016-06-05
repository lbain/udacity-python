from twilio.rest import TwilioRestClient
from secrets import secret_numbers

message = raw_input("What do you need to remember?\n")

information = secret_numbers()
account_sid = information['twilio']['account_sid']
auth_token  = information['twilio']['auth_token']

client = TwilioRestClient(account_sid, auth_token)

client.messages.create(body=message,
    to=information['my_number'],
    from_=information['twilio']['phone_number'])

print("Reminded you to {0}".format(message))
