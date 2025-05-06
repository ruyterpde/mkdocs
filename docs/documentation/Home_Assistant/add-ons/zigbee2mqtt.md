---
Title: Installing Zigbee2MQTT in Home Assistant
Summary: A step-by-step guide to installing and configuring the Zigbee2MQTT add-on in Home Assistant.
Author:
  - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Zigbee2MQTT

## Installing Zigbee2MQTT in Home Assistant
A clear and concise guide for setting up Zigbee2MQTT in Home Assistant.

## Overview
Zigbee2MQTT allows you to connect Zigbee devices with Home Assistant without relying on proprietary hubs. This guide will walk you through the installation and configuration process.

### Technical Details
Zigbee2MQTT requires a Zigbee adapter compatible with the software. Common adapters include:
- **CC2531**
- **CC2652**
- **Sonoff ZBDongle**
  
The add-on requires MQTT to function properly, which must be installed and configured in Home Assistant before proceeding.

### Infobox
| **Component**      | **Description**                                                        |
| ------------------ | ---------------------------------------------------------------------- |
| Zigbee2MQTT Add-on | Enables direct communication between Zigbee devices and Home Assistant |
| MQTT Broker        | Required for Zigbee2MQTT to relay messages                             |
| Zigbee Coordinator | USB adapter to connect Zigbee devices                                  |

### Steps
1. **Install MQTT Broker**: Ensure the MQTT add-on is installed and running.
2. **Install Zigbee2MQTT Add-on**:
   - Open Home Assistant.
   - Navigate to **Settings** > **Add-ons**.
   - Search for **Zigbee2MQTT** and install it.
3. **Configure Zigbee2MQTT**:
   - Open the Zigbee2MQTT add-on configuration.
   - Set the MQTT broker details.
   - Define the serial port used by the Zigbee adapter ([See Sonoff](../hardware/sonoff.md)).

    ```
    port: >-
      /dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_V2_d2c4d0ccfc73ef119820e21e313510fd-if00-port0
    adapter: ember
    ```

4. **Restart the Add-on**: Apply changes and restart Zigbee2MQTT.
5. **Pair Devices**: Place Zigbee devices in pairing mode and add them to Zigbee2MQTT.

### Commands
```sh
# Check Zigbee2MQTT logs
docker logs zigbee2mqtt

# Restart Zigbee2MQTT
docker restart zigbee2mqtt
```

### Examples
```yaml
mqtt:
  host: "mqtt-broker.local"
  port: 1883
zigbee:
  serial:
    port: "/dev/ttyUSB0"
```

### Resources
- [Official Zigbee2MQTT Documentation](https://www.zigbee2mqtt.io/){:target="_blank"}
- [Home Assistant Add-ons Guide](https://www.home-assistant.io/addons/){:target="_blank"}
- [Installation Zigbee2MQTT on Github](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt#installation){:target="_blank"}

### Troubleshooting
#### Issue: Zigbee2MQTT Not Connecting
- Ensure the serial port is correctly set.
- Verify MQTT broker credentials.

#### Issue: Devices Not Pairing
- Reset the Zigbee device.
- Bring the device closer to the coordinator.
- Restart Zigbee2MQTT and attempt pairing again.

---

*Generated using AI*