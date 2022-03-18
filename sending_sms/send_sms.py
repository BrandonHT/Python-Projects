from twilio.rest import Client

account_sid = 'AC73e613f70e11a5c627654fc2da655da6' 
auth_token = 'db937aa815c734e7e3596f26b3515949' 
client = Client(account_sid, auth_token) 

message = client.messages.create(  
        messaging_service_sid='MG18711c91c6dcf32f84248553137e2cd8', 
        body='this actually works!',      
        to='+525628253359' 
    )

print(message.sid)