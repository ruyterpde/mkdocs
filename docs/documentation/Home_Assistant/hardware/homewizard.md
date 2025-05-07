---
Title: HomeWizard P1 Meter Installation and Integration with Home Assistant
Summary: Guide to installing and integrating the HomeWizard P1 meter into Home Assistant.
Author:
    - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# HomeWizard

## HomeWizard P1 Meter Installation and Integration with Home Assistant

## Overview
This guide details the installation and configuration of the HomeWizard P1 meter within Home Assistant, ensuring seamless integration for real-time energy monitoring.

## Technical Details
HomeWizard P1 meter connects via Wi-Fi to provide smart energy readings. Integration with Home Assistant allows automated control and analytics. Recommended setup includes:
- HomeWizard P1 meter
- Home Assistant running on Raspberry Pi or similar
- Wi-Fi connectivity

## Infobox
| Feature       | Description                         |
| ------------- | ----------------------------------- |
| Compatibility | Works with Home Assistant (via API) |
| Connectivity  | Wi-Fi enabled                       |
| Power Supply  | USB-powered                         |
| Data Refresh  | Real-time energy monitoring         |

## Steps
### 1. Install HomeWizard P1 Meter
- Connect HomeWizard P1 meter to the P1 port of the energy meter.
- Power the device using USB adapter.
- Ensure proper Wi-Fi connection.

### 2. Configure Home Assistant
- Navigate to **Settings > Integrations** in Home Assistant.
- Search for **HomeWizard Energy** and install the integration.
- Enter the local IP address of the P1 meter.
- Save and restart Home Assistant.

### 3. Validate Data Flow
- Navigate to **Developer Tools > States** and confirm sensor data visibility.
- Add **P1 meter entities** to Home Assistant dashboard.

## Commands
```yaml
sensor:
  - platform: homewizard
    host: "192.168.x.x"
    monitored_conditions:
      - total_power
      - voltage
```

## Examples
### Example Automation
```yaml
automation:
  - alias: Notify on Power Spike
    trigger:
      - platform: numeric_state
        entity_id: sensor.homewizard_power
        above: 3000
    action:
      - service: notify.mobile_app
        data:
          message: "Power consumption is unusually high!"
```

## Resources
- [HomeWizard P1 Meter](https://www.homewizard.com/nl/p1-meter)
- [HomeWizard P1 API Documentation](https://homewizard.com/api)
- [Home Assistant Integration Guide](https://www.home-assistant.io/integrations/homewizard/)

## Troubleshooting
### Issue: Data Not Appearing in Home Assistant
**Solution:** Ensure the IP address is correct and check network connectivity.

### Issue: Integration Fails
**Solution:** Restart Home Assistant and reinstall the HomeWizard integration.

---

*Generated using AI*