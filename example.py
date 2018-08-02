#ABP Example
from iotloranode import loraNode
#Setup the Node
node = loraNode()
node.set_appEUI("70B3D57ED00089C7")
node.set_devAddr("26011BFD")
node.set_networkKey("BDCB202742D0C9A7EA0F834CCE5BCFFE")
node.set_appSessionKey("A7C13B3BA8CDB07368F40F5E871F799F")
node.send_string_packet("Hello World")
