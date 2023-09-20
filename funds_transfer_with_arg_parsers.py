import argparse
import subprocess

# Define a function to get the headers from the USSD server.
def get_headers():

  # Get the response from the API.
  response = subprocess.run(['curl', '-k', '-s', '-H', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9', 'http://192.168.8.1/api/ussd/send'], stdout=subprocess.PIPE)

  # Extract the cookie and token from the headers.
  cookie = response.stdout.decode('utf-8').split('\n')[0].split(';')[0]
  token = response.stdout.decode('utf-8').split('\n')[1].split('=')[1]

  return cookie, token

# Define a function to get a curl command for the specified URL, cookie, and token.
def get_curl_command(url, cookie, token):

  # Return the curl command.
  return ['curl', '-X', 'POST', url, '-H', 'Cookie: {}'.format(cookie), '-H', 'x-requested-with: XMLHttpRequest', '-H', '__RequestVerificationToken: {}'.format(token)]

# Define a function to execute the curl commands.
def execute_curl_commands(curl_commands):

  # Execute the curl commands.
  for curl_command in curl_commands:
    subprocess.run(curl_command)

if __name__ == '__main__':

  # Create an argument parser.
  parser = argparse.ArgumentParser(description='Send an USSD request to the specified phone number.')

  # Add an argument for the phone number to send the USSD request to.
  parser.add_argument('--phone-number', required=True, help='The phone number to send the USSD request to.')

  # Add an argument for the amount to transfer.
  parser.add_argument('--amount', required=True, help='The amount to transfer.')

  # Add an argument for the pin code to authenticate the transaction.
  parser.add_argument('--pin-code', required=True, help='The pin code to authenticate the transaction.')

  # Parse the command-line arguments.
  args = parser.parse_args()

  # Get the cookie and token from the USSD server.
  cookie, token = get_headers()

  # Create a list of curl commands.
  curl_commands = [
    get_curl_command('*126#', cookie, token),
    get_curl_command('1', cookie, token),
    get_curl_command('1', cookie, token),
    get_curl_command('Enter the targets phone number', cookie, token),
    get_curl_command('Enter the Amount {}'.format(args.amount), cookie, token),
    get_curl_command('1', cookie, token),
    get_curl_command('Enter the Pin {}'.format(args.pin_code), cookie, token),
    get_curl_command('Click on the "Submit" button', cookie, token)
  ]

  # Execute the curl commands.
  execute_curl_commands(curl_commands)
