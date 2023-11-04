# First of all import the socket library
import socket
import pandas as pd # In case of error, install pandas using: pip install pandas
# Create an empty Pandas DataFrame
df = pd.DataFrame(columns=['Temp', 'Humd', 'Label']) # Label: 1 means valid, 0 means invalid
# Next create a socket object
s = socket.socket()
print ("Socket successfully created")
# Reserve a port on your computer in our
# Case it is 12345 but it can be anything
port = 12345
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket binded to %s" %(port))
# Put the socket into listening mode
s.listen(5)
print ("socket is listening")
# Establish connection with client.
c, addr = s.accept()
print ('Got connection from', addr)
# A forever loop until we interrupt it or
# an error occurs
i = 300 # Only 10 reading will be taken. Increase it to higher according to your plan.
while i>=0:
# Receive data from client
    client = c.recv(1024)
    data = client.decode()
    temp = data.split(" ")[0]
    hum = data.split(" ")[1]
    new_data = {
        'Temp': temp,
        'Humd': hum,
        'Label': 1
                }
    df = df._append(new_data, ignore_index=True)
    #Print it
    print(data)
    print(i)
    i = i - 1
# Close the connection with the client
c.close()
# Export data to CSV
df.to_csv('data.csv', index=False)