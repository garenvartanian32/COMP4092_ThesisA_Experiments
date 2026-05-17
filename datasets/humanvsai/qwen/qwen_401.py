def process_connection(connection, my_socket):
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break
            process_data(data)
        except Exception as e:
            print(f'Error occurred: {e}')
            break
        check_timers()
    connection.close()
    my_socket.close()

def process_data(data):
    """Process the received data."""
    print(f'Received data: {data}')

def check_timers():
    """Check and handle timers."""
    print('Checking timers...')
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)