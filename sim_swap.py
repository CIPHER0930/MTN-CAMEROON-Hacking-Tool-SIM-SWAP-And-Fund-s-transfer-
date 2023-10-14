import requests
import json

# Set the URL of the USSD send endpoint
URL = "http://192.168.8.1/api/ussd/send"

# Extract cookies and headers from the URL
response = requests.get(URL, allow_redirects=False)
cookies = response.headers["Set-Cookie"]
headers = response.headers

# Set the phone number and SMS message
# PHONE_NUMBER = "7147"
# SMS_MESSAGE = "RECONDUCT 678738373 679847447 12345678 9876543210 500"

# Get the old phone number from the user
old_phone_number = input("Enter your old phone number: ")

# Get the new phone number from the user
new_phone_number = input("Enter your new phone number: ")

# Get the serial number of the new SIM card from the user
new_sim_card_serial_number = input("Enter the serial number of the new SIM card: ")

# Get the PUK code of the new SIM card from the user
new_sim_card_puk_code = input("Enter the PUK code of the new SIM card: ")

# Get one of the last 5 numbers you called from the user
last_called_number = input("Enter one of the last 5 numbers you called: ")

# Get the amount of your last recharge from the user
last_recharge_amount = input("Enter the amount of your last recharge: ")

# Construct the SMS message
sms_message = f"RECONDUCT {new_phone_number} {new_sim_card_serial_number} {new_sim_card_puk_code} {last_called_number} {last_recharge_amount}"

# Create the cURL command
curl_command = f"curl -X POST {URL} -d '{json.dumps({'phoneNumber': '7147', 'message': sms_message})}'"

# Add cookies and headers to the cURL command
curl_command = f"{curl_command} -H '{json.dumps(headers)}' -b '{json.dumps(cookies)}'"

# Execute the cURL command
curl_output = requests.post(curl_command)

# Check the cURL output
if curl_output.status_code == 200 and curl_output.json()["status"] == "success":
    print("Successfully sent SMS to 7147")
else:
    print(f"Failed to send SMS to 7147: {curl_output.text}")
    exit(1)
