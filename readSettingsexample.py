#read Example
from iotloranode import loraNode
#Setup the Node
node = loraNode()

print(node.get_devAddr())
print(node.get_devEUI())
print(node.get_appEUI())
print(node.get_appKey())
print(node.get_networkKey())
print(node.get_appSessionKey())
print(node.get_loraPower())
print(node.get_adrMode())
print(node.get_spreadingFactor())
