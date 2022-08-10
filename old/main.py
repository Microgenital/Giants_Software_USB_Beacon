import time
import hid

# Vendor and product ID for the device we want to talk to
VENDOR_GIANTS = 0x340d
PRODUCT_BEACON = 0x1710

# Data packages to send to the device
LEDS_ON_ROUND = [0x00, 0xFF, 0x01, 0x66, 0xC8, 0xFF, 0xAD, 0x52, 0x81, 0xD6]
LEDS_ON_BLINK = [0x00, 0xFF, 0x07, 0xFF, 0x64, 0xFF, 0xEB, 0x7D, 0x9A, 0x03]
LEDS_OFF = [0x00, 0xFF, 0x00, 0x00, 0x64, 0x00, 0x32, 0x9E, 0xD7, 0x0D]

# Show all connected USB devices
"""
for device_dict in hid.enumerate():
    keys = list(device_dict.keys())
    keys.sort()
    for key in keys:
        print("%s : %s" % (key, device_dict[key]))
    print()
"""

try:
    # Connect to the device
    print("Opening the device")
    h = hid.device()
    h.open(VENDOR_GIANTS, PRODUCT_BEACON)

    print("Manufacturer: %s" % h.get_manufacturer_string())
    print("Product: %s" % h.get_product_string())
    print("Serial No: %s" % h.get_serial_number_string())

    # enable non-blocking mode
    h.set_nonblocking(1)

    # write some data to the device
    print("Write the data")
    # stay on
    while True:
        h.write(LEDS_ON_BLINK)  # Turn on the LEDs (Use LEDS_ON_ROUND or LEDS_ON_BLINK)
        time.sleep(3)

# Turn off the LEDs when the program is interrupted
except KeyboardInterrupt:
    h.write(LEDS_OFF)
    print("Closing the device")
    h.close()

except IOError as ex:
    print(ex)
    print("You probably don't have the hard-coded device.")
    print("Update the h.open() line in this script with the one")
    print("from the enumeration list output above and try again.")

print("Done")
