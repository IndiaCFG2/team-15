from twilio.rest import Client


# put your own credentials here
def send_message(st):
	account_sid = "AC93d243be0c91e79419773eae3f2e3ac2"
	auth_token = "c4d033e20ab84e23bc26fa151d82810f"
	client = Client(account_sid, auth_token)
	client.messages.create(
	  to="+918557921442",
	  from_="+12015817241",
	  body="Your lesson link is: " + st
	  )

send_message('123')
