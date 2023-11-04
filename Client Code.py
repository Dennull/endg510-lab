# Import socket module
import socket
# Import time module
import time
# Import Adafruit module
import Adafruit_DHT
# Create a socket object
s = socket.socket()
# Define the port on which you want to connect
port = 12345
# Connect to the server on local computer
s.connect(('172.20.10.4', port)) # Use your laptop IP
while True:
	# Read from sensor
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	# Prepare data
	data = str(temperature) + " " + str(humidity)
	print (data)
	# Send data to the server
	s.send(data.encode())
	# Pause for 1 second
	time.sleep(1)
# Close the channel
s.close()
