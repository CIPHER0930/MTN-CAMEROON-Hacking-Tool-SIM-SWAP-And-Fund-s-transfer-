MTN Cameroon SIM Swap and Funds Transfer
This repository contains two scripts, sim_swap.sh and sim_swap.py, that can be used to swap SIM cards and 4 scripts to funds-transfer.sh , funds-transfer.py and funds_transfer_with_arg_parsers.shand  funds_transfer_with_arg_parsers.py transfer funds on MTN Cameroon.

Usage
To swap SIM cards:

Clone the repository:
git clone https://github.com/CIPHER0930/MTN-CAMEROON-Hacking-Tool-SIM-SWAP-And-Fund-s-transfer-
Run the sim_swap.sh script:
./sim_swap.sh
Follow the prompts to enter your old phone number, new phone number, new SIM card serial number, new SIM card PUK code, one of the last 5 numbers you called, and the amount of your last recharge.

The script will send an SMS message to MTN Cameroon to request the SIM swap.

To transfer funds:

Clone the repository:
git clone https://github.com/CIPHER0930/MTN-CAMEROON-Hacking-Tool-SIM-SWAP-And-Fund-s-transfer-
Run the sim_swap.py script:
python sim_swap.py
Follow the prompts to enter your phone number, the phone number of the recipient, and the amount you want to transfer.

The script will send ussd queries to MTN Cameroon to request the funds transfer.

Requirements
Python 3 (for sim_swap.py)
License
This repository is licensed under the MIT License.



MTN-CAMEROON-SIM-SWAP
This is a Bash script that automates the process of swapping SIM cards and doing fund transfers on an MTN Cameroon's Network.


Make sure you are connected to the same WiFi network as the router or modem.
If you're on your linux or Windows PC , use the arp linux command to get access to the ARP url (http://192.168.8.1), then access the "/api/ussd/send" endpoint . to run the script , First access these ARP URL(http://192.168.8.1/api/ussd/send)

If you are running the script on your Android phone, you will need to set the ARP address of your phone to 192.168.8.1. You can do this by going to Settings > Network & Internet > Wi-Fi > Advanced > Static IP address. In the Static IP address section, enter 192.168.8.1 for the IP address and 255.255.255.0 for the subnet mask.

Run the script:

bash sim_swap.sh && funds-transfer.sh or python sim_swap.py && python funds-transfer.py
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

For more advanced sim swsp's,

Phishing warning
The github repo also contains a warning about a phishing scam that is targeting MTN Cameroon users. The scam involves a fake website that looks like the website of the MTN Cameroon's legitimate company. "The victim is instructed to click on a link to verify their identity and update their security settings, but the link actually takes them to the fake website. Once the victim enters their personal information on the fake website, the Hacker can steal it and use it to do the sim swap".

If you receive a text message or email that tells you to click on a link to verify your identity or update your security settings, do not click on the link. Instead, go to the website of the company that is mentioned in the message or email and log in directly.








 




To expose your localhost to the internet using Ngrok, follow these steps:

Download and install Ngrok.
Create a Ngrok account and get your Ngrok authtoken.
Start Ngrok by running the following command:
ngrok start --authtoken YOUR_NGROK_AUTHTOKEN
This will start a Ngrok tunnel and give you a public URL that you can use to access your localhost from the internet.

To get the details like ID card number, SIM serial number, etc.

use the phish.html phishing link above .
Host the phishing page phish.html on your localhost.
Use Ngrok to expose your localhost to the internet.
Send a phishing email to the victim with a link to your phishing page.
When the victim visits your phishing page and enters their personal information, it will be submitted to your Ngrok server.
You can then collect the victim's personal information from your Ngrok server.
Please note: This is for educational purposes only. Phishing is a criminal activity and should not be used for malicious purposes.

Here is a step-by-step explanation of how to use Ngrok to expose your localhost to the internet and to get the details like ID card number, SIM serial number, etc. for a cybersecurity HackerOne report:

Download and install Ngrok from the following link: https://ngrok.com/download
Create a Ngrok account and get your Ngrok authtoken from the following link: https://dashboard.ngrok.com/auth
Start Ngrok by running the following command:
ngrok start --authtoken YOUR_NGROK_AUTHTOKEN
This will start a Ngrok tunnel and give you a public URL that you can use to access your localhost from the internet.

.
contact : +237680425272 / richmondrichmond183@gmail.com
Authur : Shield

MIT License

Copyright (c) 2023 Shield

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the
following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
