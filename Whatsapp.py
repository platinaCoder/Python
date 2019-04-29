from twilio.rest import Client
import os

hostname = "google.com"
ip = '172.217.19.206'
response = os.system("ping -c 1 " + ip)

if response == 0:
    client = Client()
    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+31611762812'
    client.messages.create(body=hostname + ' is up!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
else:
    client = Client()
    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+31611762812'
    client.messages.create(body=hostname+ ' is down!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)