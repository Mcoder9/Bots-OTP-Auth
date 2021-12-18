import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://api.telegram.org/bot5025578400:AAGFk-Pn2s8ldowlKR6aqLjzRlO88Lgnak0'

def send_msg(data,result):
    chat_id = result['message']['chat']['id']
    replytext = f'<pre>{json.dumps(result, indent = 4)}</pre>'
    parameters = {
        "chat_id" : chat_id,
        "parse_mode": 'html',
        "text" : replytext
    }
    resp = requests.get(base_url + '/sendMessage', data = parameters)
    if resp.status_code == 200:
        print('replyed ok!')
    


def read_latest(offset):
    parameters = {
        "offset" : offset
    }
    resp = requests.get(base_url + '/getUpdates', data = parameters)
    data = resp.json()
    print('Bot is running...!')
    
    for result in data['result']:
        text = result['message']['text']
        if text == '/info' or text == '/start':
            send_msg(data,result)
    
    
    if data['result']:
        return data['result'][-1]['update_id']+1

offset = 0
while True:
    offset = read_latest(offset)
