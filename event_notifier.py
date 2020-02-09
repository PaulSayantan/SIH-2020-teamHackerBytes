import datetime
import json
import requests

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

with open('event.json') as json_data:
    data = json.load(json_data)

with open('phone.json') as json_data:
    phones = json.load(json_data)

def sendPostRequest(reqUrl, apiKey, secretKey, useType, person_name, evnt_name, date, phoneNo, senderId, textMessage):
      req_params = {
  'apikey':'MO0BQE8ORQ6MMM703929OCN80FYST0MJ',
  'secret':'D5OVWMD1ABMIW31W',
  'usetype':'stage',
  'phone': phoneNo,
  'message':"Dear {}, This message is just a reminder that the next meeting for {} will be held on {}. --Regards Poshan-Abhiyaan ".format(person_name, evnt_name, date),
  'senderid': 'SMSIND'
  }
      return requests.post(reqUrl, req_params)

event_new = {}
for event in data:
    event_date = event[0].split('.')
    day = event_date[0]
    month = event_date[1]
    year = event_date[2]
    event_name = event[1]
    event_new[year+'-'+month+'-'+day] = event_name

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

currentDT = datetime.datetime.now()
d1 = currentDT.strftime("%Y-%m-%d")

from datetime import datetime
notifier_diff1 = 30
for d2 in event_new.keys():
    evnt_name = event_new[d2]
    if days_between(d1, d2) <= notifier_diff1:
        for user in phones:
            person_name = user[0]
            person_phoneNo = user[1]
            response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', person_name, evnt_name, d2, person_phoneNo, 'active-sender-id', 'message-text' )
            print(response.text)
        notifier_diff1 = int(notifier_diff1/2)
