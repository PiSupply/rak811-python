#Pi Supply IoT LoRa Node Library
#ABP Connection Example

#Import The Library
from iotloranode import loraNode

#Setup the node module
node = loraNode()

#Set the node address, network key and app sesion key from lora provider
node.set_devAddr("26011FD8")
node.set_networkKey("2E6292746E6905BFF64B6DAA2A983ADF")
node.set_appSessionKey("23C9BC60EBED5998F09E83C4BF70CAA8")

#Join on ABP network
node.join(node.abp)

#Set the spreading factor to SF7
node.set_spreadingFactor(7)

#Send a string
node.send_string_packet("Hello World")
