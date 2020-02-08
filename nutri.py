import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

with open('carb.json') as json_data:
    data = json.load(json_data)

def sendPostRequest(reqUrl, apiKey, secretKey, useType, person_name,person_age, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':'GONH3SSENF7LFSKCH2CYO25AHUYGITU5',
  'secret':'U6OGI5LEL57EYWSZ',
  'usetype':'stage',
  'phone': phoneNo,
  'message':"{} Age: {}, According to your latest medical report, you have been deprived of carbohydrates in your diet. Please visit your nearest Poshan-Abhiyaan Camp as soon as possible.".format(person_name, person_age),
  'senderid': 'SMSIND'
  }
  return requests.post(reqUrl, req_params)

for person in data:
    person_name = person[1]+" "+person[2]
    person_age = person[3]
    person_phoneNo = person[5]
    response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', person_name, person_age, person_phoneNo, 'active-sender-id', 'message-text' )
    print(response.text)
