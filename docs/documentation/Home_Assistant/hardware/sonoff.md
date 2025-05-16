---
Title: How to Flash Sonoff Zigbee 3.0 USB Dongle Plus-E V2 to Ember
Summary: A step-by-step guide to flashing the Sonoff Zigbee 3.0 USB Dongle Plus-E V2 with Ember firmware.
Author:
    - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Sonoff

## How to Flash Sonoff Zigbee 3.0 USB Dongle Plus-E V2 to Ember

## Sub-title
Learn how to flash the Sonoff Zigbee 3.0 USB Dongle Plus-E V2 with Ember firmware and integrate it into your smart home setup.

## Overview
This guide provides detailed instructions for flashing the Sonoff Zigbee 3.0 USB Dongle Plus-E V2 with Ember firmware. The process includes downloading the necessary tools, preparing the hardware, and integrating the dongle with Home Assistant.

### Technical Details
The Sonoff Zigbee 3.0 USB Dongle Plus-E V2 is a versatile Zigbee coordinator based on the Silicon Labs EFR32MG21 chip. Flashing it with Ember firmware enhances compatibility with Zigbee2MQTT and ZHA (Zigbee Home Automation).

#### Requirements:
- **Hardware**: Sonoff Zigbee 3.0 USB Dongle Plus-E V2, USB extension cable (optional)
- **Software**: Ember firmware, Zigbee Firmware Flasher tool
- **System**: Windows, macOS, or Linux

### Infobox
| **Feature**               | **Details**                              |
|---------------------------|------------------------------------------|
| **Device**                | Sonoff Zigbee 3.0 USB Dongle Plus-E V2   |
| **Firmware**              | Ember                                    |
| **Integration**           | Home Assistant, Zigbee2MQTT              |
| **Tools Required**        | Zigbee Firmware Flasher, Terminal        |

### Steps
1. **Download Firmware and Tools**:
   - Visit the [Zigbee Firmware Repository](https://github.com/Koenkk/Z-Stack-firmware) to download the Ember firmware and flashing tool.
   - Install any required USB drivers.

2. **Prepare the USB Dongle**:
   - Connect the dongle to your computer.
   - Verify the device is recognized (e.g., check Device Manager on Windows).

3. **Flash the Firmware**:
   - Open a terminal and navigate to the flashing tool directory.
   - Run the flashing command:
     ```sh
     python3 flash.py --port <COM_PORT> --firmware <FIRMWARE_FILE>
     ```
   - Replace `<COM_PORT>` and `<FIRMWARE_FILE>` with appropriate values.

4. **Verify the Flash**:
   - Reconnect the dongle and verify the firmware version:
     ```sh
     python3 flash.py --port <COM_PORT> --verify
     ```

5. **Integrate with Home Assistant**:
   - Plug the dongle into the Home Assistant device.
   - Add the ZHA integration and configure the serial port.

### Commands
#### Flashing Command
```sh
python3 flash.py --port <COM_PORT> --firmware <FIRMWARE_FILE>
```

#### Verification Command
```sh
python3 flash.py --port <COM_PORT> --verify
```

### Examples
#### Example: Flashing on Windows
```sh
python3 flash.py --port COM3 --firmware ember_firmware.bin
```

#### Example: Flashing on Linux
```sh
python3 flash.py --port /dev/ttyUSB0 --firmware ember_firmware.bin
```

#### Another approach
- [How To Update the Sonoff Dongle E to Ember firmware](https://www.youtube.com/watch?v=x1QeNPi6tK8)

Configuration in Home Assistant:
```
    port: >-
      /dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_V2_d2c4d0ccfc73ef119820e21e313510fd-if00-port0
    adapter: ember
```

### Resources
- [Sonoff Zigbee 3.0 USB Dongle Documentation](https://sonoff.tech/)
- [Zigbee2MQTT Setup Guide](https://www.zigbee2mqtt.io/)
- [Home Assistant ZHA Integration](https://www.home-assistant.io/integrations/zha/)
- [Sonoff Zigbee 3.0 USB Dongle Plus-E V2](https://www.sonoff.nl/a-69235043/zigbee-producten/sonoff-zigbee-3-0-dongle-plus-e/#description)
- [Sonoff Zigbee 3.0 USB Dongle Firmware Download](https://github.com/darkxst/silabs-firmware-builder/tree/main/firmware_builds/zbdonglee)
- [Sonoff Zigbee 3.0 USB Dongle Firmware Flasher](https://darkxst.github.io/silabs-firmware-builder/)

### Troubleshooting
#### Issue: Device Not Recognized
- Ensure drivers are installed.
- Try a different USB port or cable.

#### Issue: Flashing Fails
- Double-check the COM port and firmware file path.
- Ensure no other applications are using the dongle.

#### Issue: Zigbee Devices Not Pairing
- Verify Zigbee channel settings.
- Reset and re-pair devices.

---

*Generated using AI*