"""
This file takes care of the client side of the p2p network
This file takes care of downloading file to the machine
"""


from server_client.constants import *


class Client:
    def __init__(self, addr):
        # Set up socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Allow python to use recently closed socket
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Connect
        self.s.connect((addr, PORT))

        self.previous_data = None

        # Create to work on a different thread
        i_thread = threading.Thread(target = self.send_message)
        i_thread.daemon = True
        i_thread.start()

        # Send message requesting data
        while True:
            r_thread = threading.Thread(target = self.receive_message)
            r_thread.start()
            r_thread.join()

            data = self.receive_message()

            if not data:
                # Server failed
                print("-" * 20 + " Server failed " + "-" * 20)
                break

            elif data[0:1] == b'\x11':
                # First byte is '\x11' added to make sure there are peers
                print("Got peers")
                self.update_peers(data[1:])

    """
    This function deals with printing the received message
    """
    def receive_message(self):
        try:
            print('RECEIVING ' + '-' * 8)
            data = self.s.recv(BYTE_SIZE)
            print('\nRECEIVED ' + '-' * 8)
            
            
            if self.previous_data != data:
                fileIO.create_file(data)
                self.previous_data = data
    
            return data
        except KeyboardInterrupt:
            self.send_disconnect_signal()

    """
    This method updates the list of peers
    """
    def update_peers(self, peers):
        # Peers list contain a bunch of IPs
        # -1 to remove the last value which would be None
        p2p.peers = str(peers, "utf-8").split(',')[:-1]
    
    """
    This method sends the message
    :param: msg -> The optional message to send 
    """
    def send_message(self):
        try:
            self.s.send(REQUEST_STRING.encode('utf-8'))

        except KeyboardInterrupt as e:
            self.send_disconnect_signal()
            return

    def send_disconnect_signal(self):
       print("DISCONNECTED")

       # signal the server that the connection has closed
       self.s.send("q".encode('utf-8'))
       sys.exit()