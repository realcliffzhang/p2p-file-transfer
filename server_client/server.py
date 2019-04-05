"""
This file takes part of the server side of the p2p network
This file deals with uploading of the song for other peers
"""


from server_client.constants import *


class Server: 
    def __init__(self, msg):
        try:
            # The message to upload in bytes
            self.msg = msg

            # Define a socket
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Make a list of connections
            self.connections = []

            # Make a list of peers 
            self.peers = []

            # Bind the socket
            self.s.bind((HOST, PORT))

            # Listen for connection
            self.s.listen(1)

            print("-" * 20 + "Server Running"+ "-" * 20)
            
            self.run()
        except Exception as e:
            sys.exit()

    """
    This function deals with sending info to the clients
    This function closes the connection if the client has left
    :param: connection -> The connection that the server is connected to
    :param: a -> (ip address, port) of the system connected
    """
    def handler(self, connection, a):
        try:
            while True:
                # Server receives the message
                data = connection.recv(BYTE_SIZE)
                for connection in self.connections:

                    # Connected peer wants to disconnect
                    if data in data.decode('utf-8')[0].lower() == 'q':

                        # Disconnect the peer
                        self.disconnect(connection, a)
                        return

                    # Active connection
                    elif data and data.decode('utf-8')[0] == REQUEST_STRING:
                        print('-' * 20 + ' UPLOADING ' + '-' * 20)

                        # Upload file
                        connection.send(self.msg)

        except Exception as e:
            sys.exit()

    """
    This method is use to run the server
    This method creates a different thread for each client
    """
    def run(self):
        # Constantly listeen for connections
        while True:
            connection, a = self.s.accept()

            # Append to the list of peers 
            self.peers.append(a)
            print("Peers are: {}".format(self.peers) )
            self.send_peers()

            # Create a thread for a connection
            c_thread = threading.Thread(target=self.handler, args=(connection, a))
            c_thread.daemon = True
            c_thread.start()
            self.connections.append(connection)
            print("{}, connected".format(a))
            print("-" * 50)

    """
    send a list of peers to all the peers that are connected to the server
    """
    def send_peers(self):
        peer_list = ""
        for peer in self.peers:
            peer_list = peer_list + str(peer[0]) + ","

        for connection in self.connections:
            # Byte '\x11' added at the beginning of the byte 
            # This can differentiate if user recieved a message or a list of peers
            data = PEER_BYTE_DIFFERENTIATOR + bytes(peer_list, 'utf-8')
            connection.send(PEER_BYTE_DIFFERENTIATOR + bytes(peer_list, 'utf-8'))


    """
        This function runs when peer disconnects
    """
    def disconnect(self, connection, a):
        self.connections.remove(connection)
        self.peers.remove(a)
        connection.close()
        self.send_peers()
        print("{}, disconnected".format(a))
        print("-" * 50)