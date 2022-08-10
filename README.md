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
    while True:
        h.write(LEDS_ON_ROUND)
```

To make the LEDs blink all at once use:
```python
    while True:
        h.write(LEDS_ON_BLINK)
```

## Thanks
Thanks to "steve228uk". His [Gist](https://gist.github.com/steve228uk/873d653f1ecec0456ea3f475b6e54f68) helped me a lot to understand whats going on.


## License
[MIT](https://github.com/Microgenital/Giants_Software_USB_Beacon/blob/master/LICENSE.md)