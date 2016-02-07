Python - Network Programming
Python provides two levels of access to network services. At a low level, you can access the basic socket support in the underlying operating system, which allows you to implement clients and servers for both connection-oriented and connectionless protocols.
Python also has libraries that provide higher-level access to specific application-level network protocols, such as FTP, HTTP, and so on.
This tutorial gives you understanding on most famous concept in Networking - Socket Programming
What are Sockets?
Sockets are the endpoints of a bidirectional communications channel. Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.
Sockets may be implemented over a number of different channel types: Unix domain sockets, TCP, UDP, and so on. The socket library provides specific classes for handling the common transports as well as a generic interface for handling the rest.
Sockets have their own vocabulary:
Term
Description
domain
The family of protocols that will be used as the transport mechanism. These values are constants such as AF_INET, PF_INET, PF_UNIX, PF_X25, and so on.
type
The type of communications between the two endpoints, typically SOCK_STREAM for connection-oriented protocols and SOCK_DGRAM for connectionless protocols.
protocol
Typically zero, this may be used to identify a variant of a protocol within a domain and type.
hostname
The identifier of a network interface:
∙        A string, which can be a host name, a dotted-quad address, or an IPV6 address in colon (and possibly dot) notation
∙        A string "<broadcast>", which specifies an INADDR_BROADCAST address.
∙        A zero-length string, which specifies INADDR_ANY, or
∙        An Integer, interpreted as a binary address in host byte order.
port
Each server listens for clients calling on one or more ports. A port may be a Fixnum port number, a string containing a port number, or the name of a service.
The socket Module:
To create a socket, you must use the socket.socket() function available in socketmodule, which has the general syntax:
s = socket.socket (socket_family, socket_type, protocol=0)
Here is the description of the parameters:
∙        socket_family: This is either AF_UNIX or AF_INET, as explained earlier.
∙        socket_type: This is either SOCK_STREAM or SOCK_DGRAM.
∙        protocol: This is usually left out, defaulting to 0.
Once you have socket object, then you can use required functions to create your client or server program. Following is the list of functions required:
Server Socket Methods:
Method
Description
s.bind()
This method binds address (hostname, port number pair) to socket.
s.listen()
This method sets up and start TCP listener.
s.accept()
This passively accept TCP client connection, waiting until connection arrives (blocking).
 
Client Socket Methods:
Method
Description
s.connect()
This method actively initiates TCP server connection.
General Socket Methods:
Method
Description
s.recv()
This method receives TCP message
s.send()
This method transmits TCP message
s.recvfrom()
This method receives UDP message
s.sendto()
This method transmits UDP message
s.close()
This method closes socket
socket.gethostname()
Returns the hostname.
A Simple Server:
To write Internet servers, we use the socket function available in socket module to create a socket object. A socket object is then used to call other functions to setup a socket server.
Now call bind(hostname, port function to specify a port for your service on the given host.
Next, call the accept method of the returned object. This method waits until a client connects to the port you specified, and then returns a connection object that represents the connection to that client.
 
 
 
 
 
 
 
#!/usr/bin/python           # This is server.py file
 
import socket               # Import socket module
 
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
 
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection
A Simple Client:
Now we will write a very simple client program which will open a connection to a given port 12345 and given host. This is very simple to create a socket client using Python's socket module function.
The socket.connect(hosname, port ) opens a TCP connection to hostname on the port.
Once you have a socket open, you can read from it like any IO object. When done, remember to close it, as you would close a file.
The following code is a very simple client that connects to a given host and port, reads any available data from the socket, and then exits:
#!/usr/bin/python           # This is client.py file
 
import socket               # Import socket module
 
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
 
s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done
Now run this server.py in background and then run above client.py to see the result.
# Following would start a server in background.
$ python server.py &
 
# Once server is started run client as follows:
 
$ python client.py
This would produce following result:
Got connection from ('127.0.0.1', 48437)
Thank you for connecting
Python Internet modules
A list of some important modules which could be used in Python Network/Internet programming.
Protocol
Common function
Port No
Python module
HTTP
Web pages
80
httplib, urllib, xmlrpclib
NNTP
Usenet news
119
nntplib
FTP
File transfers
20
ftplib, urllib
SMTP
Sending email
25
smtplib
POP3
Fetching email
110
poplib
IMAP4
Fetching email
143
imaplib
Telnet
Command lines
23
telnetlib
Gopher
Document transfers
70
gopherlib, urllib
Please check all the libraries mentioned above to work with FTP, SMTP, POP, and IMAP protocols.
 
