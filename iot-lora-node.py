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
    def set_devAddr(self,devAddr):
        """Set Device Address"""
    def set_devEUI(self,devEui):
        """Set Device EUI"""
    def set_appEUI(self,appEui):
        """Set Application EUI"""
    def set_appKey(self,appKey):
        """Set Application Key"""
    def set_networkKey(self,nwsk):
        """Set Network Key"""
    def set_appSessionKey(self,apsk):
        """Set Application Session Key"""
    def set_loraPower(self,pwr):
        """Set Lora Power Level"""
    def set_adrMode(self,adr):
        """Set Adaptive Data Rate"""
    def set_spreadingFactor(self,sf):
        """Set Spreading Factor"""


    ############
    # Get Settings Functions
    ############
    def get_devAddr(self):
        """Get Device Address"""
    def get_devEUI(self):
        """Get Device EUI"""
    def get_appEUI(self):
        """Get Application EUI"""
    def get_appKey(self):
        """Get Application Key"""
    def get_networkKey(self):
        """Get Network Key"""
    def get_appSessionKey(self):
        """Get Application Session Key"""
    def get_loraPower(self):
        """Get Lora Power Level"""
    def get_adrMode(self):
        """Get Adaptive Data Rate"""
    def get_spreadingFactor(self):
        """Get Spreading Factor"""
    ############
    # LoRa Functions
    ############
    def join_request(self):
        """Join over OTAA"""
    def send_raw_packet(self,packet):
        """Send raw bytes packet"""
    def sent_string_packet(self,string):
        """Send a string packet"""
    def send_int_packet(self,int):
        """Send integer packet"""
    def recieve_packet(self):
        """Check To See if there is any response"""
    ############
    # GPIO Functions
    ############
    def gpio_setmode(self,pin,mode):
        """Set Pin GPIO Mode"""
    def gpio_read(self,pin):
        """Read RAK811 GPIO"""
    def gpio_write(self,pin,state):
        """RAK811 GPIO Write Command"""
    def gpio_adc(self,pin):
        """Read RAK811 ADC"""
