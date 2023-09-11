#!/bin/bash

# Define the get_headers function
function get_headers() {
  # Get the response from the API
  response=$(curl -k -s -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9" 'http://192.168.8.1/api/ussd/send')

  # Extract the cookie and token from the headers
  cookie=$(echo "$response" | grep -E '^Set-Cookie: ' | cut -d ';' -f1 | cut -d '=' -f2)
  token=$(echo "$response" | grep -E '__RequestVerificationToken:' | cut -d '=' -f2)

  # Return the cookie and token
  echo "$cookie" "$token"
}

# Define the get_curl_command function
function get_curl_command() {
  # Get the function arguments
  local url=$1
  local cookie=$2
  local token=$3

  # Return the curl command
  echo "curl -X POST '$url' -H 'Cookie: $cookie' -H 'x-requested-with: XMLHttpRequest' -H '__RequestVerificationToken: $token'"
}

# Define the execute_curl_commands function
function execute_curl_commands() {
  

  # Execute the curl commands
  for curl_command in $curl_commands; do
    echo "$curl_command"
    curl -s "$curl_command" > /dev/null
  done
}

# Get the cookie and token
cookie, token=$(get_headers)

# Get the curl commands
curl_commands=$(
  get_curl_command '*126#' "$cookie" "$token"
  get_curl_command '1' "$cookie" "$token"
  get_curl_command '1' "$cookie" "$token"
  get_curl_command 'Enter the targets phone number' "$cookie" "$token"
  get_curl_command 'Enter the Amount ' "$cookie" "$token"
  get_curl_command '1' "$cookie" "$token"
  get_curl_command 'Enter the Pin' "$cookie" "$token"                                                                                                                                               
  #get_curl_command '' "$cookie" "$token"
  get_curl_command 'Click on the "Submit" button' "$cookie" "$token"
)

# Execute the curl commands
execute_curl_commands "$curl_commands"      
