"""
# IOT LoRa Node Python Library - Used to interface to RAK811 Boards with Micropython/Python 3.X
# Copyright (C) 2018 Pi Supply
# Written by Ryan Walmsley (Ryan@pi-supply.com)
# Designed for Raspberry Pi, Beaglebone, ESP32 & Microbit
"""

#Import the serial library for the respective platform

#Raspberry Pi

#Beaglebone

#ESP32

#Microbit

class iotloranode(object):
    """RAK811 Interface Library - Converts inputs given to serial commands for RAK811"""

    def __init__(self, region=1):
        """Initialise The Library and connect to the module"""

    ############
    # UART Functions
    ############


    ############
    # Set Settings Functions
    ############
    def set_devAddr(self,address):
        """Set Device Address"""
    def set_devEUI(self,address):
        """Set Device EUI"""
    def set_appEUI(self,address):
        """Set Application EUI"""
    def set_appKey(self,address):
        """Set Application Key"""
    def set_networkKey(self,address):
        """Set Network Key"""
    def set_appSessionKey(self,address):
        """Set Application Session Key"""
    def set_loraPower(self,address):
        """Set Lora Power Level"""
    def set_DevAddr(self,address):
        """Set Device Address"""
    def set_DevAddr(self,address):
        """Set Device Address"""


    ############
    # Get Settings Functions
    ############

    ############
    # LoRa Transmit Functions
    ############

    ############
    # GPIO Functions
    ############
