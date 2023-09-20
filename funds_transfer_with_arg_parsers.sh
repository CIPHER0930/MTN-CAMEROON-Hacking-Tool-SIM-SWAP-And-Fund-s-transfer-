#!/bin/bash

# Define a function to get the headers from the USSD server.
function get_headers() {

  # Get the response from the API.
  response=$(curl -k -s -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9" http://192.168.8.1/api/ussd/send)

  # Extract the cookie and token from the headers.
  cookie=$(echo "$response" | sed -n '1p' | cut -d ';' -f 1)
  token=$(echo "$response" | sed -n '2p' | cut -d '=' -f 2)

  echo "$cookie,$token"
}

# Define a function to get a curl command for the specified URL, cookie, and token.
function get_curl_command() {

  # Return the curl command.
  echo "curl -X POST $url -H 'Cookie: $cookie' -H 'x-requested-with: XMLHttpRequest' -H '__RequestVerificationToken: $token'"
}

# Define a function to execute the curl commands.
function execute_curl_commands() {

  # Execute the curl commands.
  for curl_command in $curl_commands; do
    eval "$curl_command"
  done
}

# Parse the command-line arguments.
getopts ":p:a:n:" args

# Get the phone number, amount, and pin code from the command-line arguments.
phone_number="${OPTARG_p}"
amount="${OPTARG_a}"
pin_code="${OPTARG_n}"

# Get the cookie and token from the USSD server.
cookie=$(get_headers)

# Create a list of curl commands.
curl_commands=(
  $(get_curl_command "*126#")
  $(get_curl_command "1")
  $(get_curl_command "1")
  $(get_curl_command "Enter the targets phone number")
  $(get_curl_command "Enter the Amount $amount")
  $(get_curl_command "1")
  $(get_curl_command "Enter the Pin $pin_code")
  $(get_curl_command "Click on the \"Submit\" button")
)

# Execute the curl commands.
execute_curl_commands
