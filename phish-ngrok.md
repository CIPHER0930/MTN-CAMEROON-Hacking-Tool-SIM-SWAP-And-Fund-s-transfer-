Here's How to Expose the phish.html to the internet from your localhost 
Install ngrok. You can download the ngrok client for your operating system from the ngrok website: https://ngrok.com/download.
Start ngrok. In your terminal, navigate to the directory where you installed ngrok and run the following command:
ngrok http 8080
This will start ngrok and create a tunnel to your local web server(localhost), which is listening on port 8080.
3. Open the ngrok dashboard. In your browser, go to the ngrok dashboard: https://dashboard.ngrok.com/. You should see a list of tunnels that ngrok has created.
4. Find the tunnel for your local web server. The tunnel name will start with http:// or https://.
5. Open the tunnel URL in your browser. This will open your HTML file in your browser.

Now, anyone on the internet can access your HTML file by visiting the ngrok tunnel URL.

Here are some additional things to keep in mind:

The port number that you specify in the ngrok http command must be the same port number that your local web server is listening on.
If you are using a firewall, you may need to configure it to allow traffic to the port number that you are using.
The ngrok tunnel will only be active for as long as ngrok is running. If you want to keep the tunnel active, you can run ngrok in the background.
