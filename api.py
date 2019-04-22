import requests
from requests.auth import HTTPBasicAuth

# API Key
# EPUsCcvuQKWN6SJnrLfi

with open('key.txt', 'r') as f:
	key = f.read()

api_key = key
url = 'https://www.quandl.com/api/v3/datasets'
product = 'EOD'
stock = 'HD'
form = 'json'

request = url + '/' + product + '/' + stock + '.' + form + '?api_key=' + api_key
response = requests.get(request)
print(response.content)