---
Title: Creating a Custom Sensor for Counting Lights in Home Assistant
Summary: Learn how to create a custom sensor in Home Assistant to calculate the number of lights currently turned on and display it on a dashboard.
Author:
    - Peter de Ruyter
Date: 2025-05-04
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Lights Sensor

## Creating a Custom Sensor for Counting Lights in Home Assistant
   This guide explains how to create a custom sensor in Home Assistant that calculates the number of lights currently turned on. The sensor can be displayed on a dashboard for quick monitoring.

## Overview
   Home Assistant allows users to monitor and control lights in their home. By creating a custom template sensor, you can calculate the number of lights that are currently turned on and display this information on your dashboard.

### Technical Details
   - **Sensor Type**: Template Sensor
   - **Functionality**: Counts the number of lights in the `on` state.
   - **Dashboard Integration**: The sensor is added to a dashboard for easy monitoring.

### Infobox
   - **Sensor Name**: `number_lights_on`
   - **Friendly Name**: Number Lights On
   - **Icon**: `mdi:lightbulb-group`
   - **Use Case**: Monitor the number of active lights in your home.

### Steps
   1. **Define the Template Sensor**:
      Add the following configuration to your `configuration.yaml` file:
      ```yaml
      template:
        - sensor:
            - name: "Number Lights On"
              friendly_name: "Number Lights On"
              value_template: >-
                {{ states.light
                      | rejectattr('attributes.entity_id', 'defined')
                      | selectattr('state', 'eq', 'on')
                      | list | count }}
              icon_template: mdi:lightbulb-group
      ```

   2. **Restart Home Assistant**:
      - Restart Home Assistant to apply the changes.

   3. **Add to Dashboard**:
      - Go to your dashboard and add a **Gauge Card** or **Entities Card**.
      - Select the `sensor.number_lights_on` sensor to display the number of lights currently turned on.

### Commands
   - **Restart Home Assistant**:
     ```bash
     ha core restart
     ```
   - **Check Configuration**:
     ```bash
     ha core check
     ```

### Examples
   - **Template Sensor Output**:
     - If 3 lights are turned on, the sensor will display: `3`.

   - **Dashboard Example**:
     - Add a **Gauge Card** to visually represent the number of lights turned on.

### Resources
   - [Templates and Custom Sensors in Home Assistant](https://www.youtube.com/watch?v=cdz32TLu_gw)
   - [Home Assistant Template Sensors](https://www.home-assistant.io/integrations/template/)
   - [Home Assistant Light Integration](https://www.home-assistant.io/integrations/light/)
   - [Dashboard Customization](https://www.home-assistant.io/lovelace/)

### Troubleshooting
   - **Issue**: The sensor always shows `0`.  
     **Resolution**: Ensure that your lights are correctly integrated into Home Assistant and that their states are being updated.

   - **Issue**: Configuration errors after adding the template sensor.  
     **Resolution**: Use the `ha core check` command to validate your configuration.

---

*Generated using AI*