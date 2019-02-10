# IOT LoRa Node Python Library - Used to interface to RAK811 Boards
# with Micropython/Python 3.X
# Copyright (C) 2018 Pi Supply
# Written by Ryan Walmsley (Ryan@pi-supply.com)
# Designed for Raspberry Pi

import binascii
from time import sleep

class loraNode:

    """RAK811 Interface Library - Converts inputs"""
    """given to serial commands for RAK811"""
    loraNodeSerialBaud = 115200
    serialLib = 0
    serial_write = None
    serial_read = None
    serLib = None
    abp = "abp"
    otaa = "otaa"
    EU868 = "EU868"
    US915 = "US915"

    def __init__(self, region=1):
        """Initialise The Library and connect to the module"""
        # Import the serial library for the respective platform

        import serial
        from RPi import GPIO
        GPIO.setwarnings(False)
        self.serLib = serial.Serial("/dev/serial0", self.loraNodeSerialBaud)
        self.serial_write = self.serLib.write
        self.serial_read = self.serLib.readline
        self.serialLib = 1
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.OUT)
        GPIO.output(17,0)
        sleep(0.01)
        GPIO.output(17,1)

        self.serLib.readline()
        self.serLib.readline()
        self.serLib.readline()
        self.set_spreadingFactor(0)

        self.serLib.readline()

    ############
    # UART Functions
    ############
    def uart_tx(self, command):
        """Takes the command and sends it via UART via the correct library"""
        # First add at to the beginning
        command = "at+%s\r\n" % command
        #print(command)
        self.serial_write(str.encode(command))

        line = self.serLib.readline()
        #print(line)
        return line

    def uart_rx(self):
        line = self.serLib.readline()
        #print(line)
        return line
        """Returns serial data"""

    ############
    # Set Settings Functions
    ############
    def set_devAddr(self, devAddr):
        """Set Device Address"""
        command = "set_config=dev_addr:%s" % devAddr
        self.uart_tx(command)

    def set_devEUI(self, devEui):
        """Set Device EUI"""
        command = "set_config=dev_eui:%s" % devEui
        self.uart_tx(command)

    def set_appEUI(self, appEui):
        """Set Application EUI"""
        command = "set_config=app_eui:%s" % appEui
        self.uart_tx(command)

    def set_appKey(self, appKey):
        """Set Application Key"""
        command = "set_config=app_key:%s" % appKey
        self.uart_tx(command)

    def set_networkKey(self, nwsk):
        """Set Network Key"""
        command = "set_config=nwks_key:%s" % nwsk
        self.uart_tx(command)

    def set_appSessionKey(self, apsk):
        """Set Application Session Key"""
        command = "set_config=apps_key:%s" % apsk
        self.uart_tx(command)

    def set_loraPower(self, pwr):
        """Set Lora Power Level"""
        command = "set_config=pwr_level:%s" % pwr
        self.uart_tx(command)

    def set_adrMode(self, adr):
        """Set Adaptive Data Rate"""
        command = "set_config=adr:%s" % adr
        self.uart_tx(command)

    def set_spreadingFactor(self, sf):
        """Set Spreading Factor"""
        command = "dr=%s" % sf
        self.uart_tx(command)

    def set_region(self, sf):
        """Set LoRaWAN Region"""
        command = "band=%s" % sf
        self.uart_tx(command)

    ############
    # Get Settings Functions
    ############

    def get_devAddr(self):
        """Get Device Address"""
        command = "get_config=dev_addr"

        return str(self.uart_tx(command)).split("OK")[1].split("\\")[0]

    def get_devEUI(self):
        """Get Device EUI"""
        command = "get_config=dev_eui"
        return str(self.uart_tx(command)).split("OK")[1].split("\\")[0]



    def get_appEUI(self):
        """Get Application EUI"""
        command = "get_config=app_eui"
        return str(self.uart_tx(command)).split("OK")[1].split("\\")[0]


    def get_appKey(self):
        """Get Application Key"""
        command = "get_config=app_key"
        return str(self.uart_tx(command)).split("OK")[1].split("\\")[0]


    def get_networkKey(self):
        """Get Network Key"""
        command = "get_config=nwks_key"
        return str(self.uart_tx(command)).split("OK")[1].split("\\")[0]

    def get_appSessionKey(self):
        """Get Application Session Key"""
        command = "get_config=apps_key"
        return str(self.uart_tx(command)).split("OK")[1].split("\\")[0]


    def get_loraPower(self):
        """Get Lora Power Level"""
        command = "get_config=pwr_level"
        return str(self.uart_tx(command)).split("OK")[1].split("\\")[0]


    def get_adrMode(self):
        """Get Adaptive Data Rate"""
        command = "get_config=adr"
        return str(self.uart_tx(command)).split("OK")[1].split("\\")[0]


    def get_spreadingFactor(self):
        """Get Spreading Factor"""
        command = "get_config=dr"
        return str(self.uart_tx(command)).split("OK")[1].split("\\")[0]


    ############
    # LoRa Functions
    ############
    def join(self, mode):
        """Join"""
        if(mode == self.abp):
            command = "join=abp"
            self.uart_tx(command)
        elif(mode == self.otaa):
            command = "join=otaa"
            self.uart_tx(command)
            # Extra response from otaa join
            line = self.serLib.readline()
            return True

    def send_raw_packet(self, packet, port):
        """Send raw bytes packet"""

    def send_string_packet(self, string, port=1, pktType=0):
        """Send a string packet"""
        command = "send=%s,%s,%s" % (pktType, port,
                                     binascii.hexlify(string.encode())
                                     .decode("utf-8"))
        self.uart_tx(command)
        # There will be an extra response
        line = self.serLib.readline()
        return line

    def send_int_packet(self, int, port):
        """Send integer packet"""

    def recieve_packet(self):
        """Check To See if there is any response"""

    def reset_radio(self):
        """Reset the RAK811 Radio Module"""
        command = "reset=0"
        self.uart_tx(command)
        self.uart_rx()
        self.uart_rx()
        self.uart_rx()


    def lora_mode(self, mode):
        """Change between LoRaWAN & LoRaP2P Modes"""

    def lora_band(self, band):
        """Set LoRaWAN Region"""
        command = "band="+band
        self.uart_tx(command)


    ############
    # GPIO Functions
    ############
    def gpio_setmode(self, pin, mode):
        """Set Pin GPIO Mode"""

    def gpio_read(self, pin):
        """Read RAK811 GPIO"""

    def gpio_write(self, pin, state):
        """RAK811 GPIO Write Command"""

    def gpio_adc(self, pin):
        """Read RAK811 ADC"""
