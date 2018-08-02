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
    def set_adrMode(self,address):
        """Set Adaptive Data Rate"""
    def set_spreadingFactor(self,address):
        """Set Spreading Factor"""


    ############
    # Get Settings Functions
    ############
    def get_devAddr(self,address):
        """Get Device Address"""
    def get_devEUI(self,address):
        """Get Device EUI"""
    def get_appEUI(self,address):
        """Get Application EUI"""
    def get_appKey(self,address):
        """Get Application Key"""
    def get_networkKey(self,address):
        """Get Network Key"""
    def get_appSessionKey(self,address):
        """Get Application Session Key"""
    def get_loraPower(self,address):
        """Get Lora Power Level"""
    def get_adrMode(self,address):
        """Get Adaptive Data Rate"""
    def get_spreadingFactor(self,address):
        """Get Spreading Factor"""
    ############
    # LoRa Functions
    ############
    def join_request(self):
        """Join over OTAA"""
    def send_raw_packet(self,address):
        """Send raw bytes packet"""
    def sent_string_packet(self,address):
        """Send a string packet"""
    def send_int_packet(self,address):
        """Send integer packet"""
    def recieve_packet(self,address):
        """Check To See if there is any response"""
    ############
    # GPIO Functions
    ############
    def gpio_setmode(self,address):
        """Set Pin GPIO Mode"""
    def gpio_read(self,address):
        """Set Device EUI"""
    def gpio_write(self,address):
        """Set Application EUI"""
    def gpio_adc(self,address):
        """Set Application Key"""   
