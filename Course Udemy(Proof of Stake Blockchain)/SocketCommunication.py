from p2pnetwork.node import Node
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector
from BlockchainUtils import BlockchainUtils
import json


class SocketCommunication(Node):
    def __init__(self,ip,port):
        super(SocketCommunication,self).__init__(ip,port,None)
        self.peers=[]
        self.peerDiscoveryHandler=PeerDiscoveryHandler(self)
        self.socketConnector=SocketConnector(ip,port)

    def connectToFirstNode(self):
        if self.socketConnector.port != 10001:
            self.connect_with_node('localhost',10001)


    def startSocketCommunication(self,node):
        self.node=node
        self.start()
        self.peerDiscoveryHandler.start()
        self.connectToFirstNode()
    
    def inbound_node_connected(self, connected_node):
        print("inbound connection")
        self.peerDiscoveryHandler.handshake(connected_node)
        self.send_to_node(connected_node,"Hi I am the node you are connected to")

        # return super().inbound_node_connected(connected_node)
    def outbound_node_connected(self, connected_node):
        print("outbound connection")
        self.peerDiscoveryHandler.handshake(connected_node)
        # self.send_to_node(connected_node,"Hi I am the node who initialized the connection")
        
    

    def node_message(self, connected_node, message):
        message=BlockchainUtils.decode(json.dumps(message))
        

        if not type(message) == type("message"):
            if message.messageType == "DISCOVERY":
                self.peerDiscoveryHandler.handleMessage(message)
            elif message.messageType == "TRANSACTION":
                transaction=message.data
                self.node.handleTransaction(transaction)

    
    def send(self,recevier,message):
        self.send_to_node(recevier,message)
    
    def broadcast(self,message):
        self.send_to_nodes(message)

