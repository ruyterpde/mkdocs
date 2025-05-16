---
Title: Installation and Configuration of Mosquitto Broker in Home Assistant
Summary: A comprehensive guide to setting up and configuring Mosquitto Broker in Home Assistant as part of MQTT.
Author:
  - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Mosquitto Broker

## Installation and Configuration of Mosquitto Broker in Home Assistant
Integrate Mosquitto Broker with Home Assistant to enable seamless MQTT communication.

## Overview
Mosquitto is a lightweight MQTT broker that enables IoT devices to communicate efficiently via the MQTT protocol. This guide outlines the installation and configuration process within Home Assistant.

### Technical Details
Mosquitto operates as an MQTT broker, facilitating message exchanges between clients. Configuration in Home Assistant includes authentication, topic management, and SSL security settings.

### Infobox
| Feature          | Description                                |
| ---------------- | ------------------------------------------ |
| Broker           | Mosquitto MQTT Broker                      |
| Protocol         | MQTT                                       |
| Home Assistant   | Compatible via MQTT integration            |
| Security         | Supports authentication and SSL encryption |

### Steps
#### Install Mosquitto Broker Add-on
1. Navigate to **Home Assistant > Settings > Add-ons**.
2. Search for **Mosquitto Broker** and click **Install**.
3. Once installed, start the add-on and review the logs for confirmation.

#### Configure Mosquitto in Home Assistant
1. Enable **MQTT integration** in Home Assistant.
2. Set up authentication credentials (username/password) in `configuration.yaml`.
3. Restart Home Assistant for changes to take effect.

### Commands
#### Verify Mosquitto Installation
```sh
mosquitto -v
```

#### Test Connection
```sh
mosquitto_sub -h localhost -t "home/assistant"
mosquitto_pub -h localhost -t "home/assistant" -m "Hello MQTT"
```

### Examples
#### Example MQTT Configuration in Home Assistant
```yaml
mqtt:
  broker: localhost
  username: homeassistant
  password: securepassword
```

### Resources
- [Mosquitto Official Documentation](https://mosquitto.org/documentation/)
- [Home Assistant MQTT Integration](https://www.home-assistant.io/integrations/mqtt/)

### Troubleshooting
#### Issue: MQTT Broker Not Starting
- Check logs in **Home Assistant > Settings > Add-ons > Mosquitto Broker**.
- Ensure correct credentials are set in `configuration.yaml`.
- Restart Home Assistant.

#### Issue: Devices Not Connecting
- Validate MQTT topics with `mosquitto_sub` and `mosquitto_pub`.
- Check firewall settings to allow MQTT traffic.

---

*Generated using AI*