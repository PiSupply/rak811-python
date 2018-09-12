# IOT LoRa Node Python Library - Used to interface to RAK811 Boards
# with Micropython/Python 3.X
# Copyright (C) 2018 Pi Supply
# Written by Ryan Walmsley (Ryan@pi-supply.com)
# Designed for Raspberry Pi, Beaglebone, ESP32 & Microbit


import binascii


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

    def __init__(self, region=1):
        """Initialise The Library and connect to the module"""
        # Import the serial library for the respective platform

        if(self.serialLib == 0):
            # Should be RPi or Beaglebone
            try:
                import serial
                self.serLib = serial.Serial("/dev/ttyUSB0",
                                            self.loraNodeSerialBaud)
                self.serial_write = self.serLib.write
                self.serial_read = self.serLib.readline
                self.serialLib = 1
            except ModuleNotFoundError:
                print("Error importing Raspberry Pi")
                pass

        if(self.serialLib == 0):
            # Microbit Micropython
            try:
                import uart
                self.serLib = uart
                self.serLib.init(self.loraNodeSerialBaud, tx=14, rx=15)
                self.serial_write = uart.write
                self.serial_read = uart.readline
                self.serialLib = 2
            except ModuleNotFoundError:
                print("Error importing Microbit")
                pass

        # ESP32
        # Not doing esp yet
        if(self.serialLib == 0):
            print("Error! No Serial Library Detected")
        self.reset_radio()
        self.set_spreadingFactor(5)

    ############
    # UART Functions
    ############
    def uart_tx(self, command):
        """Takes the command and sends it via UART via the correct library"""
        # First add at to the beginning
        command = "at+%s\r\n" % command
        print(command)
        self.serial_write(str.encode(command))
        line = self.serLib.readline()
        print(line)

    def uart_rx(self):
        line = self.serLib.readline()
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
    def join(self, mode):
        """Join"""
        if(mode == self.abp):
            command = "join=abp"
            self.uart_tx(command)
        elif(mode == self.otaa):
            print("OTAA Not Programmed In Yet")

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
        print(line)

    def send_int_packet(self, int, port):
        """Send integer packet"""

    def recieve_packet(self):
        """Check To See if there is any response"""

    def reset_radio(self):
        """Reset the RAK811 Radio Module"""
        command = "reset=0"
        self.uart_tx(command)
        self.uart_rx()

    def lora_mode(self, mode):
        """Change between LoRaWAN & LoRaP2P Modes"""

    def lora_band(self, band):
        """Set LoRaWAN Region"""

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
