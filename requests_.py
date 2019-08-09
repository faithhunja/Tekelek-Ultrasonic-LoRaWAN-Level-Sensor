import measurements_conversion
import status_conversion

import os
import json
import requests
from requests.auth import HTTPBasicAuth

os.environ["WEBLINK"] = "type_your_web_link_here"
response = requests.get(os.environ["WEBLINK"], auth=('username', 'password'))
json_data = json.loads(response.text)

for i in range(len(json_data)):
	payload =json_data[i]['data']
	if payload !='':
		if str(json_data[i]['data'])[0:2] == '30':
			print(i,"============================================")
			print("Payload = ",json_data[i]['data'])
			print("Date and time = ",json_data[i]['datetime'])
			print("Device Address = ",json_data[i]['devaddr'])
			status_conversion.ullage (payload)
			
		else:
			print(i,"============================================")
			print("Payload = ",json_data[i]['data'])
			print("Date and time = ",json_data[i]['datetime'])
			print("Device Address = ",json_data[i]['devaddr'])
			measurements_conversion.ullage (payload)
			
	
