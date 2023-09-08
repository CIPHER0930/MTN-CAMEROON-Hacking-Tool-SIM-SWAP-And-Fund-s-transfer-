import requests

def get_headers():
  response = requests.get('http://192.168.8.1/api/ussd/send', headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9'
  })
  headers = response.headers
  cookie = headers['Cookie'].split(':')[1]
  token = headers['__RequestVerificationToken']
  return cookie, token

def get_curl_command(url, cookie, token):
  return f'curl -X POST {url} -H "Cookie: {cookie}" -H "x-requested-with: XMLHttpRequest" -H "__RequestVerificationToken: {token}" -H "Content-Type:application/x-www-form-urlencoded;charset=UTF-8" -d "<Request><Content>{1}</Content><CodeType>CodeType</CodeType></Request>"'

def execute_curl_commands(curl_commands):
  for curl_command in curl_commands:
    print(curl_command)
    requests.post(curl_command)

cookie, token = get_headers()
curl_commands = [
  get_curl_command('Select the option for SIM swap', cookie, token),
  get_curl_command('Enter your old MTN Cameroon phone number', cookie, token),
  get_curl_command('Enter your National ID card number or passport number', cookie, token),
  get_curl_command('Enter the IMEI number of your phone', cookie, token),
  get_curl_command('Enter the serial number of your old SIM card', cookie, token),
  get_curl_command('Click on the "Submit" button', cookie, token)
]

execute_curl_commands(curl_commands)
