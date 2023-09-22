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

  # TODO: Implement this function to detect the type of device that the script is running on.

  return 'android'


def main():
  token_id = None

  try:
    # Get the device type.
    device_type = get_device_type()

    # If the device is a router, get the token ID.
    if device_type == 'router':
      router_url = 'http://localhost:8080'
      router_username = input('Enter router username: ')
      router_password = input('Enter router password: ')

      token_id = get_token_id(router_url, router_username, router_password)

    # Get the phone number and USSD message from the user.
    phone_number = input('Enter phone number: ')
    ussd_message = input('Enter USSD message: ')

    # Get the ARP address of the router.
    router_ip = get_router_ip(device_type)

    # If the device is an Android device, set the ARP address to 192.168.8.1.
    if device_type == 'android':
      set_arp_address(subprocess.check_output(['ip', 'link', 'show', 'wlan0']).decode().splitlines()[-1].split()[4])

    # Generate a URL payload string for the USSD message.
    url_payload = generate_url_payload('http://localhost:8080/ussd/send', {
      'message': ussd_message,
      'phone_number': phone_number,
      'router_ip': router_ip
    })

    # Send the URL payload string to the endpoint.
    response = send_ussd_message(url_payload, token_id)

    # Print the response to the USSD message.
    print(response)

  # Handle any errors that occur within the try block.
  except Exception as e:
    print(f'Failed to send USSD message: {e}')
    main()


if __name__ == '__main__':
  main()
