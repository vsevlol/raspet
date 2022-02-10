import requests
import datetime
from bs4 import BeautifulSoup

headers = {'user-agent': 'my-app/0.0.1'}  
response = requests.get(url, headers=headers)

now = datetime.datetime.now()
realchas=int(now.hour)
realmin=int( now.minute)
#MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates?offset=-1'.format(token=Token1)
#response = requests.get(MethodGetUpdates)
stro=[]
headers = {'user-agent': 'my-app/0.0.1'}  
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')


     
