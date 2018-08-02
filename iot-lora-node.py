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
    def uart_tx(self,command):
        """Takes the command and sends it via UART via the correct library"""
    def uart_rx(self):
        """Returns serial data"""
    ############
    # Set Settings Functions
    ############
    def set_devAddr(self,devAddr):
        """Set Device Address"""
        command = "set_config=dev_addr:%s" % devAddr
        self.uart_tx(command)
    def set_devEUI(self,devEui):
        """Set Device EUI"""
        command = "set_config=dev_eui:%s" % devEui
        self.uart_tx(command)
    def set_appEUI(self,appEui):
        """Set Application EUI"""
        command = "set_config=app_eui:%s" % appEui
        self.uart_tx(command)
    def set_appKey(self,appKey):
        """Set Application Key"""
        command = "set_config=app_key:%s" % appKey
        self.uart_tx(command)
    def set_networkKey(self,nwsk):
        """Set Network Key"""
        command = "set_config=nwks_key:%s" % nwsk
        self.uart_tx(command)
    def set_appSessionKey(self,apsk):
        """Set Application Session Key"""
        command = "set_config=apps_key:%s" % apsk
        self.uart_tx(command)
    def set_loraPower(self,pwr):
        """Set Lora Power Level"""
        command = "set_config=pwr_level:%s" % pwr
        self.uart_tx(command)
    def set_adrMode(self,adr):
        """Set Adaptive Data Rate"""
        command = "set_config=adr:%s" % adr
        self.uart_tx(command)
    def set_spreadingFactor(self,sf):
        """Set Spreading Factor"""
        command = "set_config=dr:%s" % sf
        self.uart_tx(command)


    ############
    # Get Settings Functions
    ############
    def get_devAddr(self):
        """Get Device Address"""
        command = "get_config=dev_addr"
        self.uart_tx(command)
    def get_devEUI(self):
        """Get Device EUI"""
        command = "get_config=dev_eui"
        self.uart_tx(command)
    def get_appEUI(self):
        """Get Application EUI"""
        command = "get_config=app_eui"
        self.uart_tx(command)
    def get_appKey(self):
        """Get Application Key"""
        command = "get_config=app_key"
        self.uart_tx(command)
    def get_networkKey(self):
        """Get Network Key"""
        command = "get_config=nwks_key"
        self.uart_tx(command)
    def get_appSessionKey(self):
        """Get Application Session Key"""
        command = "get_config=apps_key"
        self.uart_tx(command)
    def get_loraPower(self):
        """Get Lora Power Level"""
        command = "get_config=pwr_level"
        self.uart_tx(command)
    def get_adrMode(self):
        """Get Adaptive Data Rate"""
        command = "get_config=adr"
        self.uart_tx(command)
    def get_spreadingFactor(self):
        """Get Spreading Factor"""
        command = "get_config=dr"
        self.uart_tx(command)
    ############
    # LoRa Functions
    ############
    def join_request(self):
        """Join over OTAA"""
    def send_raw_packet(self,packet,port):
        """Send raw bytes packet"""
    def sent_string_packet(self,string,port):
        """Send a string packet"""
    def send_int_packet(self,int,port):
        """Send integer packet"""
    def recieve_packet(self):
        """Check To See if there is any response"""
    def reset_radio(self):
        """Reset the RAK811 Radio Module"""
    def lora_mode(self,mode):
        """Change between LoRaWAN & LoRaP2P Modes"""
    def lora_band(self,band):
        """Set LoRaWAN Region"""
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
