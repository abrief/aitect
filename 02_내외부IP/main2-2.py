import requests

def get_external_ip():
    try:
        # Use the 'httpbin' service to get the external IP address.
        response = requests.get('https://httpbin.org/ip')
        # The response contains JSON data, so parse the JSON to get the IP.
        ip = response.json()['origin']
        return ip
    except requests.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("External IP:", get_external_ip())
