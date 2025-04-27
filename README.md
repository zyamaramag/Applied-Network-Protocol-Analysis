# Applied-Network-Protocol-Analysis
This project is a Python-based brute-force tool designed to crack a PIN code for an HTTP application hosted on a specific port. It automates repeated PIN submissions and monitors server responses to detect a successful attempt. A key part of the process involved identifying the correct server address, port number, and necessary request parameters.

How to Run
Starting the Server
Launch the provided executable (.exe) file to start the server.

Open a browser and visit http://127.0.0.1:8888.

The application will then be ready to accept PIN entries.

Running the Python Script

Open the project folder in Visual Studio Code or your preferred Python IDE.

Ensure Python is installed on your system.

Install any required packages (such as requests) if needed.

Run the script from the terminal using:

python brute_force_PIN.py

The script will systematically attempt all 3-digit PINs, showing progress in the console.

Methodology
Discovering the Server Address and Port

- Wireshark was used to monitor network traffic while running the executable. Analysis revealed that the server operates on 127.0.0.1 (localhost) and listens on port 8888.

Finding the Necessary Parameters

- By tracing the HTTP stream in Wireshark, it was identified that the server expects the PIN value to be submitted using the magicNumber field. The script was tailored to match this requirement.

Performance Considerations

- While no significant technical issues were encountered, the brute-force approach naturally leads to slower PIN discovery times.

Key Takeaways

- Gained practical experience with basic brute-force techniques.

- Developed a better understanding of server-side protections against brute-force attacks.

Security Recommendations

- Increase PIN complexity by allowing letters, symbols, or longer strings.

- Implement rate limiting or account lockout mechanisms to discourage brute-force attempts.
