import requests

def get_headers():
  # Get the response from the API
  response = requests.get('http://192.168.8.1/api/ussd/send', headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9'})

  # Extract the cookie and token from the headers
  cookie = response.headers['Set-Cookie'].split(';')[0].split('=')[1]
  token = response.headers['__RequestVerificationToken']

  # Return the cookie and token
  return cookie, token

def get_curl_command(url, cookie, token):
  # Get the function arguments
  local url=url
  local cookie=cookie
  local token=token

  # Return the curl command
  return f'curl -X POST {url} -H "Cookie: {cookie}" -H "x-requested-with: XMLHttpRequest" -H "__RequestVerificationToken: {token}"'

def execute_curl_commands(curl_commands):

  # Execute the curl commands
  for curl_command in curl_commands:
    print(curl_command)
    requests.post(curl_command)

# Get the cookie and token
cookie, token = get_headers()

# Get the curl commands
curl_commands = [
  get_curl_command('*126#', cookie, token),
  get_curl_command('1', cookie, token),
  get_curl_command('1', cookie, token),
  get_curl_command('Enter the targets phone number', cookie, token),
  get_curl_command('Enter the Amount ', cookie, token),
  get_curl_command('1', cookie, token),
  get_curl_command('Enter the Pin', cookie, token),
  #get_curl_command '' "$cookie" "$token"
  get_curl_command('Click on the "Submit" button', cookie, token)
]

# Execute the curl commands
execute_curl_commands(curl_commands)
