#OTAA Example
from iotloranode import loraNode
#Setup the Node
node = loraNode()
node.lora_band(node.EU868)
node.set_devEUI("00A0E3F2CACA07A6")
node.set_appEUI("70B3D57ED0013D25")
node.set_appKey("DD7D7F38D0832E4DE8A3A3BCB1F4E884")
node.join(node.otaa)
node.set_spreadingFactor(0)
while True:
    node.send_string_packet("RTK")
