---
Title: Flashing and Installing the M5Stack Atom Echo
Summary: A step-by-step guide to flashing the the M5Stack Atom Echo with ESPHome.
Author:
    - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# M5Stack

## Flashing and Installing the M5Stack Atom Echo

## Overview
The ATOM ECHO Smart Speaker Development Kit is a Programmable Smart Speaker based on the M5ATOM design. With its compact form factor measuring only 24 * 24 * 17 mm, this speaker delivers impressive capabilities. Easily play music wirelessly using the BT capabilities of the ESP32 from your mobile phone or tablet. What sets ATOM ECHO apart is its programmability and integration with cloud platforms such as AWS and Baidu. Utilizing the built-in microphone and speaker, it enables voice interaction and AI functionality. Experience voice control, story-telling, and seamless integration with the Internet of Things (IoT). The speaker is equipped with an embedded RGB LED (SK6812), allowing for visual display of connection status. Beyond its role as a Bluetooth speaker, ATOM ECHO retains the control abilities of the Atom series. The convenient screw hole on the back facilitates easy installation for users. With ATOM ECHO, you have a powerful, programmable smart speaker that combines compact design, AI capabilities, and seamless IoT integration for an enhanced audio experience in any setting. 

### Technical Details
| Resources     | Parameter                                   |
| ------------- | ------------------------------------------- |
| SoC           | ESP-PICO-D4, 240MHz, Dual Core, Wi-Fi       |
| Flash         | 4MB                                         |
| Interface     | 1x IR-TX,1x Function Button,1x Reset Button |
| PinOut        | G21/G25/5V/GND, 3V3/G22/G19/G23/G33         |
| RGB LED       | SK6812                                      |
| Speaker       | 0.5W/NS4168 I2S                             |
| Microphone    | SPM1423 PDM                                 |
| Net weight    | 5g                                          |
| Gross weight  | 10g                                         |
| Product Size  | 24*24*17mm                                  |
| Package Size  | 63*63*12mm                                  |
| Case Material | Plastic ( PC )                              |

### Steps
1. Install ESPHome
1. Connect Atom Echo (use the right USB-C Cord)
1. Enter Network credentials
1. Skip installation (do not create config on device at this stage)
1. Select ESP32
1. Store created Encryption Key
1. SKIP
1. Replace content atom-echo.yaml

!!! warning
    NOT THE ENCRYPTION KEY

``` yaml title="atom-echo.yaml" linenums="1"
esphome:
  name: atom-echo
  friendly_name: Atom Echo

i2s_audio:
  i2s_lrclk_pin: GPIO33
  i2s_bclk_pin: GPIO19

esp32:
  board: m5stack-atom
  framework:
    type: arduino

logger:
api:
  encryption: 
    key: {use the key generated automatically}
ota:

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Atom-Echo Fallback Hotspot"
    password: "somepassword"

captive_portal:

improv_serial:
    
microphone:
  - platform: i2s_audio
    id: atom_echo_microphone
    adc_type: external
    i2s_din_pin: GPIO23
    pdm: true

voice_assistant:
  microphone: atom_echo_microphone
  on_start:
    - light.turn_on:
        id: led
        blue: 100%
        red: 0%
        green: 0%
        effect: none
  on_tts_start:
    - light.turn_on:
        id: led
        blue: 0%
        red: 0%
        green: 100%
        effect: none
  on_tts_end:
    - media_player.play_media: !lambda return x;
    - light.turn_on:
        id: led
        blue: 0%
        red: 0%
        green: 100%
        effect: pulse
  on_end:
    - delay: 1s
    - wait_until:
        not:
          media_player.is_playing: media_out
    - light.turn_off: led
  on_error:
    - light.turn_on:
        id: led
        blue: 0%
        red: 100%
        green: 0%
        effect: none
    - delay: 1s
    - light.turn_off: led

binary_sensor:
  - platform: gpio
    pin:
      number: GPIO39
      inverted: true
    name: Button
    id: echo_button
    on_multi_click:
      - timing:
          - ON FOR AT MOST 350ms
          - OFF FOR AT LEAST 10ms
        then:
          - media_player.toggle: media_out
      - timing:
          - ON FOR AT LEAST 350ms
        then:
          - voice_assistant.start:
      - timing:
          - ON FOR AT LEAST 350ms
          - OFF FOR AT LEAST 10ms
        then:
          - voice_assistant.stop:

media_player:
  - platform: i2s_audio
    id: media_out
    name: None
    dac_type: external
    i2s_dout_pin: GPIO22
    mode: mono

light:
  - platform: esp32_rmt_led_strip
    id: led
    name: None
    pin: GPIO27
    default_transition_length: 0s
    chipset: SK6812
    num_leds: 1
    rgb_order: grb
    rmt_channel: 0
    effects:
      - pulse:
          transition_length: 250ms
          update_interval: 250ms
```

1. Make use of I2S Audio Microphone
1. Save atom-echo.yaml
1. Validate
1. INSTALL
1. Plug into this computer (the one with the browser on it)
1. Select the right USB and Connect
1. Wait for a couple of minutes .....
1. Configuration Installed!
1. Settings > Devices > .....

### Commands
INFO ESPHome 2025.4.1  
INFO Reading configuration /config/esphome/atom-echo.yaml...  
INFO Starting log output from 192.168.0.106 using esphome API  
INFO Successfully connected to atom-echo @ 192.168.0.106 in 0.254s  
INFO Successful handshake with atom-echo @ 192.168.0.106 in 0.096s  
[13:17:14][I][app:100]: ESPHome version 2025.4.1 compiled on Apr 29 2025, 12:02:10

### Examples
- [LOCAL VOICE CONTROL of Home Assistant with the M5Stack Atom Echo](https://www.youtube.com/watch?v=U2rykdQlSgA)
- [media-players/m5stack/m5stack-atom-echo.yaml](https://github.com/esphome/media-players/blob/main/m5stack/m5stack-atom-echo.yaml)

### Resources
- [M5STACK ATOM ECHO Smart Speaker Development Kit](https://shop.m5stack.com/products/atom-echo-smart-speaker-dev-kit)
- [Wyoming Protocol](https://www.home-assistant.io/integrations/wyoming/)
- [Ready-Made Projects — ESPHome](https://esphome.io/projects/)
- [home-assistant/esphome-firmware](https://git.sudo.is/home-assistant/esphome-firmware/src/branch/main/voice-assistant/m5stack-atom-echo.yaml)
- [fortuna/m5stack-atom-echo.yaml](https://gist.github.com/fortuna/7de464d15ef96f4bb11c25d7f630ce89)


### Troubleshooting
!!! failure
    INFO ESPHome 2025.4.1  
    INFO Reading configuration /config/esphome/atom-echo.yaml...  
    Failed config  

``` yaml linenums="1"
binary_sensor.gpio: [source /config/esphome/atom-echo.yaml:87]  
  platform: gpio  
  pin:   
    number: GPIO39  
    inverted: True  
  name: Button  
  id: echo_button  
  on_multi_click:   
    - timing:   
        - ON FOR AT MOST 350ms  
        - OFF FOR AT LEAST 10ms  
      then:   
        -   
          {==expected a dictionary.==}

          media_player.toggle: media_out  
    - timing:   
        - ON FOR AT LEAST 350ms  
        then:  
          - voice_assistant.start:  
      - timing:  
          - ON FOR AT LEAST 350ms  
          - OFF FOR AT LEAST 10ms  
        then:  
          - voice_assistant.stop:  
```

Correct: see id media-out

``` yaml linenums="1"
binary_sensor:  
  - platform: gpio  
    pin:  
      number: GPIO39  
      inverted: true  
    name: Button  
    id: echo_button  
    on_multi_click:  
      - timing:  
          - ON FOR AT MOST 350ms  
          - OFF FOR AT LEAST 10ms  
        then:  
          - media_player.toggle:  
              id: media_out  
      - timing:  
          - ON FOR AT LEAST 350ms  
        then:  
          - voice_assistant.start:  
      - timing:  
          - ON FOR AT LEAST 350ms  
          - OFF FOR AT LEAST 10ms  
        then:  
          - voice_assistant.stop:  
```

---

*Generated using AI*