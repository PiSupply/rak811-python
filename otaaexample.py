#Pi Supply IoT LoRa Node Library
#OTAA Connection Example


#Import The Library
from iotloranode import loraNode

#Setup the Node
node = loraNode()

#Set the node dev eui, app eui and app key from LoRa Provider
node.set_devEUI("00A0E3F2CACA07A6")
node.set_appEUI("70B3D57ED0013D25")
node.set_appKey("DD7D7F38D0832E4DE8A3A3BCB1F4E884")

#Join network using OTAA
node.join(node.otaa)

#Set spreading factor to 7
node.set_spreadingFactor(7)

node.send_string_packet("Hello World!")
