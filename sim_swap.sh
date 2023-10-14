#!/bin/bash

# Extract cookies and headers from the URL
URL="http://192.168.8.1/api/ussd/send"
COOKIES=$(curl -sL -o /dev/null -w "%{http_cookie}\n" "$URL")
HEADERS=$(curl -sL -o /dev/null -w "%{header}\n" "$URL")

# Set the phone number and SMS message
# PHONE_NUMBER="7147"
# SMS_MESSAGE="RECONDUCT 678738373 679847447 12345678 9876543210 500"

# Get the old phone number from the user
echo "Enter your old phone number:"
read OLD_PHONE_NUMBER

# Get the new phone number from the user
echo "Enter your new phone number:"
read NEW_PHONE_NUMBER

# Get the serial number of the new SIM card from the user
echo "Enter the serial number of the new SIM card:"
read NEW_SIM_CARD_SERIAL_NUMBER

# Get the PUK code of the new SIM card from the user
echo "Enter the PUK code of the new SIM card:"
read NEW_SIM_CARD_PUK_CODE

# Get one of the last 5 numbers you called from the user
echo "Enter one of the last 5 numbers you called:"
read LAST_CALLED_NUMBER

# Get the amount of your last recharge from the user
echo "Enter the amount of your last recharge:"
read LAST_RECHARGE_AMOUNT

# Construct the SMS message
SMS_MESSAGE="RECONDUCT ${NEW_PHONE_NUMBER} ${NEW_SIM_CARD_SERIAL_NUMBER} ${NEW_SIM_CARD_PUK_CODE} ${LAST_CALLED_NUMBER} ${LAST_RECHARGE_AMOUNT}"

# Set the cURL command
CURL_COMMAND="curl -X POST http://192.168.8.1/api/ussd/send -d '{\"phoneNumber\":\"7147\",\"message\":\"$SMS_MESSAGE\"}'"

# Add cookies and headers to the cURL command
CURL_COMMAND="$CURL_COMMAND -H \"$HEADERS\" -b \"$COOKIES\""

# Execute the cURL command
curl_output=$(eval $CURL_COMMAND)

# Check the cURL output
if [[ $curl_output == "success" ]]; then
 echo "Successfully sent SMS to 7147"
else
 # Handle the error
 echo "Failed to send SMS to 7147: $curl_output"
 exit 1
fi
Explain these script
