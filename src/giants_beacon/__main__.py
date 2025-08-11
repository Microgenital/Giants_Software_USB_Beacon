import argparse

def main() -> None:
    """Command-line interface for controlling the USB Beacon."""
    parser = argparse.ArgumentParser(
        description="Control the Giants Software USB Beacon"
    )
    parser.add_argument(
        "state",
        choices=["round", "blink", "off"],
        help="LED behavior to set",
    )
    args = parser.parse_args()

    from . import GiantsBeacon

    beacon = GiantsBeacon()
    beacon.device_state(args.state)


if __name__ == "__main__":
    main()
