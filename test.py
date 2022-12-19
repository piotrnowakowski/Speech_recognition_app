import json
from bs4 import BeautifulSoup

with open('email_data.txt') as f:
    json_data = json.load(f)

email_data_raw = json_data['value']

email_data = []
for i in email_data_raw:
  email = {
      'id':i['id'],
      'sent_time': i['sentDateTime'],
      'hasAttachments': i['hasAttachments'],
      'subject': i['subject'],
      'importance': i['importance'],
      'conversationId': i['conversationId'],
      'conversationIndex': i['conversationIndex'],
      'text': i['body']['content'],
      'from_name': i['from']['emailAddress']['name'],
      'from_address': i['from']['emailAddress']['address'],
      'to_recipient': i['toRecipients'],
      'flag': i['flag']['flagStatus']
  }
  email_data.append(email)

for i in range(len(email_data)):
    html = email_data[i]['text']
    soup = BeautifulSoup(str(html), 'html.parser')
    text = soup.get_text()
    email_data[i]['text'] = text
print(email_data[1]['text'])
with open('result.json', 'w') as fp:

    json.dump(email_data, fp)
