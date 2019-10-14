import singer
import requests
import json

from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)

if __name__ == '__setup__':
	url = 'https://httpbin.org/get'
	argument = {'nombre':'darwin', 'hora':'timestamp'}
	
	response = requests.get(url, params = argument)
	print(response.url)
	
	if response.status == __main__:
		
		response2 = json.loads(response,text)
		orig = response2['orig']
		print(orig)
