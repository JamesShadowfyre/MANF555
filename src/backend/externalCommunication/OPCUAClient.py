from opcua import Client, ua

class OPCUAClient():
    
    def connect(self, client_address):
        try:
            self.client = Client(client_address)
            self.client.connect()
            print(" INFO : Connected to OPC-UA server at", client_address)
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
        for machineNode in nodeMap.keys():
            try:
                    node = self.client.get_node(machineNode)
                    print(node.get_browse_name())
                    node.set_value(ua.DataValue(ua.Variant(nodeMap.get(machineNode), node.get_data_type_as_variant_type())))
            except Exception as e:
                print(e)

    def read(self, nodeMap):
        for machineNode in nodeMap.keys():
            try:
                    node = self.client.get_node(machineNode)
                    nodeMap.update({machineNode: node.get_value()})
            except Exception as e:
                print(e)