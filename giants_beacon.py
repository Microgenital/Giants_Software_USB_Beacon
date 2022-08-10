import time
import hid


class GiantsBeacon:
    def __init__(self):
        """Uses the default vendor and product ID for the device we want to talk to"""
        self.VENDOR_ID = 0x340d
        self.PRODUCT_ID = 0x1710

        self.LED_OFF = [0x00, 0xFF, 0x00, 0x00, 0x64, 0x00, 0x32, 0x9E, 0xD7, 0x0D]
        self.LED_ON_BLINK = [0x00, 0xFF, 0x07, 0xFF, 0x64, 0xFF, 0xEB, 0x7D, 0x9A, 0x03]
        self.LED_ON_ROUND = [0x00, 0xFF, 0x01, 0x66, 0xC8, 0xFF, 0xAD, 0x52, 0x81, 0xD6]
        self.device = hid.device()  # initialize the device

    def get_device(self):
        # Show all connected USB devices
        for device_dict in hid.enumerate():
            keys = list(device_dict.keys())
            keys.sort()
            for key in keys:
                print("%s : %s" % (key, device_dict[key]))
            print()

    def device_state(self, state):
        """
        :param state: off, blink, round
        """
        self.device.open(self.VENDOR_ID, self.PRODUCT_ID)  # open the device
        self.device.set_nonblocking(1)  # set the device to non-blocking mode
        if state == "off":
            self.device.write(self.LED_OFF)
            self.device.close()
        elif state == "blink":
            self.device.write(self.LED_ON_BLINK)
            self.device.close()
        elif state == "round":
            self.device.write(self.LED_ON_ROUND)
            self.device.close()
        else:
            print("Invalid state")
            self.device.write(self.LED_OFF)
            self.device.close()


if __name__ == "__main__":
    Beacon = GiantsBeacon()
    Beacon.device_state("round")
    time.sleep(2)
    Beacon.device_state("blink")
    time.sleep(2)
    Beacon.device_state("off")

