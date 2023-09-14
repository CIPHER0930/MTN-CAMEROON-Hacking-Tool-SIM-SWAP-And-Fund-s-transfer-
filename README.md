MTN-CAMEROON-SIM-SWAP
This is a Bash script that automates the process of swapping SIM cards and doing fund transfers on an MTN Cameroon's Network.

Usage:

Clone this repository:
git clone https://github.com/CIPHER0930/MTN-CAMEROON-SIM-SWAP
Change directory into the repository:
cd MTN-CAMEROON-SIM-SWAP
Make sure you are connected to the same WiFi network as the router or modem.
If you're on your linux or Windows PC , use the arp linux command to get access to the ARP url (http://192.168.8.1), then access the "/api/ussd/send" endpoint . to run the script , First access these ARP URL(http://192.168.8.1/api/ussd/send)

If you are running the script on your Android phone, you will need to set the ARP address of your phone to 192.168.8.1. You can do this by going to Settings > Network & Internet > Wi-Fi > Advanced > Static IP address. In the Static IP address section, enter 192.168.8.1 for the IP address and 255.255.255.0 for the subnet mask.

Run the script:

bash SIM-SWAP.sh && funds-transfer.sh or python swap.py && python funds-transfer.py
Requirements:

Bash
curl
Instructions for setting the ARP address on an Android phone:

Open the Settings app.
Tap on Network & Internet.
Tap on Wi-Fi.
Tap on the name of the WiFi network that you are connected to.
Tap on the three dots in the top right corner.
Tap on Advanced.
Scroll down and tap on Static IP address.
Enter 192.168.8.1 for the IP address and 255.255.255.0 for the subnet mask.
Tap on Save.
Disclaimer:

NB: This script is for educational purposes only. Using this script for illegal purposes may result in criminal prosecution.

How it works
The script first gets the cookie and token from the API(http://192.168.8.1/api/ussd/send), which are needed to authenticate the requests. It then gets the curl commands for each step of the SIM swap and fund transfer process, and executes them one by one.

Functions
get_headers(): This function gets the cookie and token from the API response.
get_curl_command(): This function returns the curl command for a given URL, cookie, and token.
execute_curl_commands(): This function executes the given curl commands.
main(): This is the main function of the script. It gets the cookie and token, gets the curl commands, and executes them.
Example usage
bash script.sh
This will start the SIM swap and fund transfer process.

Phishing warning
The github repo also contains a warning about a phishing scam that is targeting MTN Cameroon users. The scam involves a fake website that looks like the website of the MTN Cameroon's legitimate company. "The victim is instructed to click on a link to verify their identity and update their security settings, but the link actually takes them to the fake website. Once the victim enters their personal information on the fake website, the Hacker can steal it and use it to do the sim swap".

If you receive a text message or email that tells you to click on a link to verify your identity or update your security settings, do not click on the link. Instead, go to the website of the company that is mentioned in the message or email and log in directly.
