import urllib.request
import socket
import g4f
# Function to interact with the ChatGPT API
def chat_with_gpt(prompt):
    response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4, messages=[
                                     {"role": "user", "content": prompt}])
    response_json = response.json()
    return response_json['choices'][0]['text'].strip()

# Function to check if a URL is a phishing URL
def is_phishing_url(url):
    prompt = f"Only respond in this format [True/False, (if true : danger in % without % symbol. if False : None)] : Is this Url a Phishing url? {url}"
    response = chat_with_gpt(prompt)
    return response

# Function to get the IP address of a URL using ip-api.com
def get_ip_address(url):
    response = requests.get(f'https://ip-api.com/json/{url}')
    response_json = response.json()
    ip_address = response_json['query']
    return ip_address

# Function to save phishing URLs to the database
def save_phishing_url(url, ip_address):
    with open('database.json', 'r+') as file:
        data = json.load(file)
        data[url] = ip_address
        file.seek(0)
        json.dump(data, file, indent=4)

# Retrieve established connections
connections = socket.net_connections()

# Iterate over the connections and check if they are open URLs
for conn in connections:
    if conn.status == 'ESTABLISHED':
        local_address = conn.laddr
        remote_address = conn.raddr

        # Check if the remote address is a valid IP and retrieve the URL
        if remote_address and remote_address.ip:
            ip = remote_address.ip
            try:
                url = urllib.request.urlopen(f"http://{ip}").geturl()
            except urllib.error.URLError:
                continue

            phishing_result = is_phishing_url(url)
            print(f"URL: {url}")
            print(f"Phishing URL: {phishing_result}")

            if phishing_result.lower() == 'true':
                ip_address = get_ip_address(url)
                save_phishing_url(url, ip_address)
                print(f"IP Address: {ip_address} saved to database.json")
