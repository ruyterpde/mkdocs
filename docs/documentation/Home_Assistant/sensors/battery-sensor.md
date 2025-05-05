---
Title: Creating a Custom Sensor for Low Battery Devices in Home Assistant
Summary: Learn how to create a custom sensor using a helper in Home Assistant to display a list of low battery devices on a dashboard.
Author:
    - Peter de Ruyter
Date: 2025-05-04
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Battery Sensor

## Creating a Custom Sensor for Low Battery Devices in Home Assistant
   This guide explains how to create a custom sensor in Home Assistant that lists devices with low battery levels. A helper is used to set the battery threshold, and the sensor is displayed on a dashboard.

## Overview
   Home Assistant allows users to monitor device battery levels. By creating a custom sensor and using a helper to define a threshold, you can easily identify devices with low battery levels and display them on your dashboard.

### Technical Details
   - **Helper**: A numeric input helper is used to set the battery threshold dynamically.
   - **Template Sensor**: A template sensor is created to check device battery levels against the threshold.
   - **Dashboard Integration**: The sensor is added to a dashboard for easy monitoring.

### Infobox
   - **Helper Type**: Numeric Input
   - **Threshold**: User-defined battery percentage (e.g., 20%)
   - **Sensor Type**: Template Sensor
   - **Use Case**: Monitor and display low battery devices.

### Steps
   1. **Create a Helper**:
      - Navigate to **Settings > Devices & Services > Helpers**.
      - Add a new **Number** helper and name it `low_battery_threshold`.
      - Set the minimum value to `0` and the maximum value to `100`.

   2. **Define a Template Sensor**:
      Add the following configuration to your `configuration.yaml` file:
      ```yaml
      template:
        - sensor:
            - name: "Low Battery Devices"
              state: >
                {% set threshold = states('input_number.low_battery_threshold') | int %}
                {% set low_battery_devices = states.sensor | selectattr('attributes.battery_level', 'defined') | selectattr('attributes.battery_level', 'lt', threshold) | map(attribute='entity_id') | list %}
                {{ low_battery_devices | join(', ') if low_battery_devices else 'None' }}
              attributes:
                devices: >
                  {% set threshold = states('input_number.low_battery_threshold') | int %}
                  {% set low_battery_devices = states.sensor | selectattr('attributes.battery_level', 'defined') | selectattr('attributes.battery_level', 'lt', threshold) | map(attribute='entity_id') | list %}
                  {{ low_battery_devices }}
      ```

   3. **Restart Home Assistant**:
      - Restart Home Assistant to apply the changes.

   4. **Add to Dashboard**:
      - Go to your dashboard and add an **Entities Card**.
      - Select the `sensor.low_battery_devices` sensor to display the list of low battery devices.

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
   - **Helper Configuration**:
     ```yaml
     input_number:
       low_battery_threshold:
         name: Low Battery Threshold
         initial: 20
         min: 0
         max: 100
         step: 1
     ```
   - **Template Sensor Output**:
     - If the threshold is set to 20%, the sensor might display: `sensor.device_1, sensor.device_2`.

### Resources
   - [Home Assistant Template Sensors](https://www.home-assistant.io/integrations/template/)
   - [Helpers in Home Assistant](https://www.home-assistant.io/docs/configuration/helpers/)
   - [Material Design Icons](https://pictogrammers.com/library/mdi)
   - [Online UUID Generator Tool](https://www.uuidgenerator.net)

### Troubleshooting
   - **Issue**: The sensor does not display any devices.  
     **Resolution**: Ensure that the devices have a `battery_level` attribute and that the helper is configured correctly.

   - **Issue**: Configuration errors after adding the template sensor.  
     **Resolution**: Use the `ha core check` command to validate your configuration.

---

*Generated using AI*