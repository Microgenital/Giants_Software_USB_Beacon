from time import sleep
import sys
from pathlib import Path

# Ensure the package in ``src`` is importable when running directly from the
# repository root.
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from giants_beacon import GiantsBeacon

beacon = GiantsBeacon()  # initialize the beacon
beacon.device_state("round")  # make the beacon go round
sleep(5)  # wait 5 seconds
beacon.device_state("blink")  # make the beacon blink
sleep(5)  # wait 5 seconds
beacon.device_state("off")  # turn the beacon off
