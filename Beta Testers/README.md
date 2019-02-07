# Beta Testers Folder
The items in this folder are intended for beta testers and will not need to be
used by normal users.

# Warning
Do not do this on 

# How To
First edit /boot/config.txt by using ```sudo nano /boot/config.txt```
Go to the bottom of the file and add in: ```dtparam=i2c_vc=on```

Now reboot.

These next commands must be run with sudo.
Next we need to enable writing to the eeprom. You can do this with running ```sudo ./eeprom_write```

Then finally we need to write to the eeprom with the file. This can be done by running ```sudo ./eepflash.sh -w -f=iotloranode.eep -t=24c32 -d=0 -a=50```

Now reboot again and try the example file in the top directory for transmitting a packet. You should see some serial responses in the form of at+ display.
