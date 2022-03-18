from twilio.rest import Client

account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 

message = client.messages.create(  
        messaging_service_sid='', # messaging service sid 
        body='this actually works!',      
        to='' # +521234567890
    )

print(message.sid)