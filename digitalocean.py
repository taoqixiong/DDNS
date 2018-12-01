import subprocess
import json
import requests

ip = subprocess.getoutput('curl -s ip.sb')
API_KEY = ''
domain_id = 'example.com'
record = ''

data = {"data": ip}
headers = {"Content-Type" : "application/json", "Authorization": "Bearer " + API_KEY }
url = "https://api.digitalocean.com/v2/domains/"+ domain_id +"/records/"+ record 
response = requests.put(url, data=json.dumps(data), headers=headers)