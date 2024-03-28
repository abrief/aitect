import socket

def get_internal_ip():
    # Attempt to connect to an Internet address, and then
    try:
        # The 'gethostbyname' function returns the current hostname,
        # and 'gethostbyname_ex' returns the IP address of that hostname
        hostname = socket.gethostname()
        # Get the internal IP based on the computer's hostname
        internal_ip = socket.gethostbyname(hostname)
        return internal_ip
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Internal IP:", get_internal_ip())
