from opcua import Client, ua
from factory.AbstractMachine import AbstractMachine

class OPCUAClient():
    
    def connect(self, client):
        try:
            self.client = Client(client.get_address())
            self.client.connect()
            print(" INFO : Connected to OPC-UA server at", self.server_addr)
        except Exception as e:
            print(" INFO : Failed to connect to OPC-UA server:", e)
    
    #ALWAYS CREATE THIS CLASS IN A TRY CATCH FINALLY, CALL THIS IN THE FINALLY BEFORE CLOSE!!!
    def disconnect(self):
        """Closes subscriptions and disconnects the OPC-UA client."""
        try:
            # Disconnect from the client
            if self.client:
                self.client.disconnect()
                print(" INFO : Disconnected from OPC-UA server")
        except Exception as e:
            print(" INFO : Error during disconnect:", e)

    def write(self, nodeMap):
        try:
            for machineNode in nodeMap.keys():
                node = self.client.get_node(machineNode)
                node.set_value(ua.DataValue(ua.Variant(nodeMap.get(machineNode), node.get_data_type_as_variant_type())))

        except Exception as e:
            print(e)

    def read(self, nodeMap):
        try:
            for machineNode in nodeMap.keys():
                node = self.client.get_node(machineNode)
                nodeMap.set(machineNode, node.get_value())

        except Exception as e:
            print(e)