import requests
import re
import subprocess

def install_arpwatch():
  """Installs ARPwatch."""
  subprocess.run(['apt', 'install', 'arpwatch'])

def start_arpwatch():
  """Starts ARPwatch monitoring the ARP cache."""
  subprocess.run(['arpwatch', '-l'])

def stop_arpwatch():
  """Stops ARPwatch monitoring the ARP cache."""
  subprocess.run(['arpwatch', '-c'])

def get_user_mac_from_arp_cache():
  """Gets the MAC address of the user from the ARP cache.

  Returns:
    A string representing the MAC address of the user, or None if the MAC address
    could not be found.
  """

  arp_output = subprocess.check_output(['arp', '-a']).decode().splitlines()

  for line in arp_output[1:]:
    ip_address, mac_address = line.split()[3:5]
    if ip_address == '192.168.8.1':
      return mac_address

  return None

def send_ussd_message_to_target_by_arp(user_mac, ussd_message, token_id, payload='my_payload'):
  """Sends a USSD message to the target ARP address.

  Args:
    user_mac: The MAC address of the target device.
    ussd_message: The USSD message to send.
    token_id: The token ID to use for authentication.
    payload: The payload to add to the USSD message.
  """

  # Escape the payload to prevent it from being interpreted as a special character in the URL.
  payload = re.escape(payload)

  # Send the USSD message.
  requests.post('http://localhost:80/send-ussd-message', json={'target_mac': user_mac, 'message': ussd_message + payload, 'token_id': token_id})

if __name__ == '__main__':
  # Install ARPwatch if it is not already installed.
  if not subprocess.run(['dpkg', '--get-selections'], stdout=subprocess.PIPE).stdout.decode().contains('arpwatch'):
    install_arpwatch()

  # Start ngrok with the following command:
  # ngrok http 80

  # Start ARPwatch monitoring the ARP cache.
  start_arpwatch()

  # Wait for a period of time to allow ARPwatch to collect ARP entries.
  subprocess.run(['sleep', '10'])

  # Stop ARPwatch monitoring the ARP cache.
  stop_arpwatch()

  # Get the MAC address of the user from the ARP cache.
  user_mac = get_user_mac_from_arp_cache()

  # If the MAC address of the user was found, send the USSD message to the ARP address 192.168.8.1.
  if user_mac:
    send_ussd_message_to_target_by_arp(user_mac, 'YOUR_USSD_MESSAGE', 'YOUR_TOKEN_ID')

  # Stop ngrok.
  subprocess.run(['pkill', 'ngrok'])
