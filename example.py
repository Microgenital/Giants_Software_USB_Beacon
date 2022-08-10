from time import sleep
import giants_beacon

beacon = giants_beacon.GiantsBeacon()  # initialize the beacon
beacon.device_state("round")  # make the beacon go round
sleep(5)  # wait 5 seconds
beacon.device_state("blink")  # make the beacon blink
sleep(5)  # wait 5 seconds
beacon.device_state("off")  # turn the beacon off
