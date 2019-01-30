# rak811-python
RAK811 Python Library for use with LoRa pHAT &amp; MicroBIT Node

Currently the library is very early on in development. At the moment you will have to do the following:

Connect via SSH or open a terminal up.

Run sudo raspi-config
Select option "5 Interfacing Options"
Then select option "P6 Serial"

It will ask you if you want a login shell to be accessible over serial, select no.
It will then ask you if you would like the serial port hardware to be enabled, select yes.

Press enter and then finish. It will ask if you would like to reboot and select yes.

It'll reboot and then either re-connect or re-open a terminal.

Next download the python file to a directory you wish, currently it isn't available via Pip but will be soon.The easiest way is to wget https://raw.githubusercontent.com/PiSupply/rak811-python/master/iotloranode.py

Finally you will need to install python serial which can be done with "sudo apt install python3-serial python3-rpi.gpio"


We're still working on the documentation and all of the functions but you can see an example at https://github.com/PiSupply/rak811-python/blob/master/example.py to get started.
