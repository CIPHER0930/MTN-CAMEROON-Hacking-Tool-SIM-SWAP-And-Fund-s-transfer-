import requests
import re
import subprocess

def get_router_ip(device_type):
  """Detects the IP address of the router that the device is connected to.

  Args:
    device_type: The type of device that the script is running on.

  Returns:
    A string representing the IP address of the router, or None if the IP address
    could not be detected.
  """

  if device_type == 'cell':
    return subprocess.check_output(['arp', '-a']).decode().splitlines()[1].split()[3]
  elif device_type == 'android':
    # Use the ngrok url payload to get and access the ARP of the Android device.
    ngrok_url = 'https://ngrok.com/api/v2/tunnels'
    response = requests.get(ngrok_url)
    ngrok_tunnel = response.json()['tunnels'][0]
    android_arp_ip = ngrok_tunnel['public_url'].replace('https://', '').replace(':443', '')

    return android_arp_ip
  else:
    return None


def set_arp_address(mac_address):
  """Sets the ARP address of the phone to 192.168.8.1.

  Args:
    mac_address: The MAC address of the phone.
  """

  subprocess.run(['arp', '-s', '192.168.8.1', mac_address])


def get_device_type():
  """Detects the type of device that the script is running on.

  Returns:
    A string representing the type of device, such as 'cell', 'android', or 'ios'.
  """

  if os.name == 'android':
    return 'android'
  else:
    return 'cell'


def get_ngrok_target_arp():
  """Gets the ARP of the ngrok target.

  Returns:
    A string representing the ARP of the ngrok target, or None if the ARP
    could not be detected.
  """

  ngrok_url = 'https://ngrok.com/api/v2/tunnels'
  response = requests.get(ngrok_url)
  ngrok_tunnel = response.json()['tunnels'][0]
  ngrok_target_arp = ngrok_tunnel['target']['addr']

  return ngrok_target_arp


def send_ussd_message_to_ngrok_target(url_payload, token_id):
  """Sends the USSD message to the ngrok target.

  Args:
    url_payload: The URL payload string for the USSD message.
    token_id: The token ID for the router.

  Returns:
    A string representing the response to the USSD message.
  """

  headers = {'Authorization': f'Bearer {token_id}'}

  # Get the ARP of the ngrok target.
  ngrok_target_arp = get_ngrok_target_arp()

  # Update the URL payload to use the ARP of the ngrok target.
  url_payload = url_payload.replace('router_ip', ngrok_target_arp)

  try:
    response = requests.post('http://localhost:8080/ussd/send', headers
