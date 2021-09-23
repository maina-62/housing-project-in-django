import requests
from datetime import datetime
import base64

from requests.auth import HTTPBasicAuth

business_shortCode ="174379"
phone_number ="254791848007"
lipa_na_mpesa_passkey="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
consumer_key="bfPiG6hbyvc0O5T3VBYymJHDDxdDuN8k"
consumer_secret="XELFJlVEtXB8vWIb"





unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
print(formatted_time,"this is formatted time")




data_to_encode = business_shortCode + lipa_na_mpesa_passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
decoded_password = encoded_string.decode("utf-8")





consumer_key = consumer_key
consumer_secret = consumer_secret

api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))


json_response = r.json()
my_access_token = json_response['access_token']



def lipa_na_mpesa(): 
    access_token = my_access_token   
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % my_access_token }
request = {
        "BusinessShortCode": business_shortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount":"1000",
        "PartyA": phone_number,
        "PartyB": business_shortCode,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://linuxinvestors.com/signup",
        "AccountReference":"12345678",
        "TransactionDesc": "pay rent"
        }
response = requests.post(api_url, json = request, headers=headers)
print(response.text)
lipa_na_mpesa()
       


  
 