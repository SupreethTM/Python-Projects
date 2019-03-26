usb = 1
driver = 1

if usb == 1:
    print('USB is CONNECTED')
    if driver == 1:
        print('Driver is installed')
    else:
        print('Driver need to install')
else:
    print('USB device not connected ')