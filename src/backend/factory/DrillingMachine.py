import AbstractMachine
from externalCommunication.OPCUAClient import OPCUAClient as OPCUAConnection

class DrillingMachine(AbstractMachine.AbstractMachine):
    
    def __init__(self):
        AbstractMachine.AbstractMachine().__init__()
        address = 'opc.tcp://172.21.3.1:4840'
        self.OPCUA = OPCUAConnection()
        self.OPCUA.connect(address)
        self.createNodeMap()
        
    def createNodeMap(self):
        #Drilling Machine Names
        self.nodeMap = {}
        self.nodeMap['ns=3;s="abstractMachine"."execOrder"' ] = True
        self.nodeMap['ns=3;s="abstractMachine"."readComplete"'] = 0
        self.nodeMap['ns=3;s="identData"."readData"[0]'] = 0
        self.nodeMap['ns=3;s="identData"."readData"[1]'] = 0
        self.nodeMap['ns=3;s="RFID_control"."write"'] = 0
        self.nodeMap['ns=3;s="RFID_control"."write_done"' ] = 0
        self.nodeMap['ns=3;s="identData"."writeData"'] = 0
        self.nodeMap['ns=3;s="abstractMachine"."TaskCode"'] = 0
        self.nodeMap['ns=3;s="abstractMachine"."numPallets"'] = 0
        self.nodeMap['ns=3;s="abstractMachine"."complete"'] = 0
    
    def execute(self, taskCode, quantity):
        self.nodeMap['ns=3;s="abstractMachine"."TaskCode"'] = taskCode
        self.nodeMap['ns=3;s="abstractMachine"."numPallets"'] = quantity
        self.nodeMap['ns=3;s="abstractMachine"."complete"'] = 0
        self.nodeMap['ns=3;s="abstractMachine"."execOrder"' ] = True
        execution = True
        #write num pallets to process and start order
        print('Pre ORder')
        self.OPCUA.write(self.nodeMap)
        while execution: 
            #write RFID info
            #Read RFID info 
            #Run Pallet process for each pallet
            self.OPCUA.read(self.nodeMap)
            returnedValues = self.nodeMap
            #Read Back Metrics info from PLC once all pallets are complete
            if returnedValues['ns=3;s="abstractMachine"."complete"'] == 1:
                execution = False
        self.nodeMap['ns=3;s="abstractMachine"."execOrder"' ] = 0
        self.OPCUA.write(self.nodeMap)
        return returnedValues

    def nameString(self):
        return "Drilling"