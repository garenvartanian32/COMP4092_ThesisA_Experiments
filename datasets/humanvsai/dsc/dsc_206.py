import socket

def request_will_echo(self):
    """Tell the DE that we would like to echo their text.  See RFC 857."""
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    port = 12345

    # connect to the DE
    s.connect(('localhost', port))

    # Send a request to echo their text
    s.send('ECHO'.encode())

    # receive data from the DE
    echo_text = s.recv(1024).decode()

    # close the connection
    s.close()

    # return the echoed text
    return echo_text