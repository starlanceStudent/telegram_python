import requests as r

telegram_token = '2123745297:AAGFyFxl2jI-si41IFQB-1-w8p2gIa-Nz4Q'
telegram_api_url = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage'
chat_id = '-768558333'
message = 'Привет от Сергея!'

params = {
	'chat_id': chat_id,
	'text': message,
}

if r.get(telegram_api_url, params):
	print(True) 
else:
	print(False)
