# Giants Software USB Beacon

This is a small script to control the Giants Software USB Beacon with Python.

## Installation

install the requirements.txt

```bash
pip install -r requirements.txt
```

## Usage
To make the LEDs light up in a circle use:

```python
import giants_beacon

Beacon = giants_beacon.GiantsBeacon()
Beacon.device_state("round")  # can be "round", "blink" or "off"
```

The device_state can be "round", "blink" or "off"

The Beacon will be turned off after 10 seconds automatically. If you want to let the beacon turn on permanently, 
just send the command "device_state" every 3 seconds. If you want to turn off the beacon earlier, just send 
device_state("off")


## Thanks
Thanks to "steve228uk". His [Gist](https://gist.github.com/steve228uk/873d653f1ecec0456ea3f475b6e54f68) helped me a lot to understand whats going on.


## License
[MIT](https://github.com/Microgenital/Giants_Software_USB_Beacon/blob/master/LICENSE.md)