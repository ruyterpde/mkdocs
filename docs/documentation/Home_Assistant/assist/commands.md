---
Title: Voice Commands in Home Assistant
Summary: A guide to using voice commands in Home Assistant for local and private smart home control.
Author:
    - Peter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Commands

## Voice Commands in Home Assistant

## Overview
Home Assistant declared 2023 the Year of the Voice, focusing on making local voice control a first-class citizen in smart home ecosystems. The goal was to bring natural, private, and fully offline voice interactions to Home Assistant, empowering users to control their homes without relying on cloud services.

## Technical Details
Home Assistant’s voice capabilities are built around the following key features:

### Assist
A new voice assistant feature introduced in Home Assistant that allows users to give voice commands locally, such as "Turn on the kitchen lights."

### Multilingual Support
Assist supports multiple languages, including English, Dutch, German, French, and more, expanding accessibility globally.

### Wake Word Integration
Home Assistant supports wake word detection using open-source solutions like Porcupine and OpenWakeWord, enabling fully hands-free interactions.

### Custom Voice Pipelines
Users can define their own voice pipelines using open-source speech-to-text (STT) and text-to-speech (TTS) engines, such as Whisper and Coqui TTS.

### ESPHome Integration
Low-cost ESP-based devices (like ESP32s with microphones and speakers) can function as voice satellites throughout the house.

## Infobox
| Feature                | Description                                  |
| ---------------------- | -------------------------------------------- |
| Assist                 | Local voice assistant for smart home control |
| Multilingual Support   | Supports multiple languages                  |
| Wake Word Integration  | Hands-free voice interactions                |
| Custom Voice Pipelines | Uses open-source STT and TTS engines         |
| ESPHome Integration    | ESP-based voice satellite devices            |

## Steps
1. Install Home Assistant.
2. Enable Assist in the Home Assistant settings.
3. Configure voice pipelines using STT and TTS engines.
  - Install Whisper (listens to you)
  - Install Piper (talks to you)
  - Install Wyoming Protocol
4. Set up wake word detection for hands-free use.
5. Integrate ESPHome-compatible voice satellite devices ([See M5Stack Atom Echo](../hardware/m5stack.md)).

## Commands
### Example Voice Commands
"Turn off all the lights in the house."
"Set the thermostat to 72 degrees."
"Is the front door locked?"
"Start the vacuum cleaner."
"Open the garage door."

## Examples
Adding a custom sentence to trigger an automation:
[Adding a custom sentence](https://www.home-assistant.io/voice_control/custom_sentences)

Customizing responses:
[Customizing responses](https://www.home-assistant.io/voice_control/custom_sentences_yaml#customizing-responses)

Audio:
Instead of the build-in speaker of the Atom Echo, you can use your own Media Player as output device.  
Add the following section into your yaml file, just after the block: on_tts_start:  
Be sure to use the right indent

``` yaml
  on_tts_end: # Addded for Media Player Output
    - homeassistant.service:
        service: media_player.play_media
        data:
          entity_id: media_player.msi_b150m
          media_content_id: !lambda 'return x;'
          media_content_type: music
          announce: "true" # Last line manual adjustment for Media Player Output
```
You also need to configure your device to be able to: Allow the device to perform Home Assistant actions.  
(last but not least, turn of the volume of the Atom Echo itself).

## Resources
- [Home Assistant Official Voice Documentation](https://www.home-assistant.io/voice_control/)
- [ESPHome Documentation](https://esphome.io/)
- [OpenWakeWord GitHub](https://github.com/openwakeword)

## Troubleshooting
!!! failure
    [12:46:25] INFO: Service exited with code 256 (by signal 4)  
    [12:46:26] WARNING: Your CPU does not support Advanced Vector Extensions (AVX). Whisper will run slower than normal.  
    [12:46:27] INFO: Service exited with code 256 (by signal 4)  
    [12:46:28] WARNING: Your CPU does not support Advanced Vector Extensions (AVX). Whisper will run slower than normal.

### Unsupported CPU
Problem, I can't run Whisper on my HA device due to the fact that my CPU doesn't support AVX.

!!! info
    The HP Compaq nc6320, equipped with an Intel  Core 2 Duo T5600 processor, does not support AVX (Advanced Vector Extensions). AVX was introduced with Intel's Sandy Bridge microarchitecture in 2011, whereas the T5600, based on the older Merom architecture, lacks this instruction set.
    If you require AVX support for specific applications, you'll need to consider upgrading to a more recent system with a compatible processor.

**Solution** Solved that problem by hosting the Whisper function on another server in my network (see [Whisper on Server](whisper.md)).

### Issue: Wake word not detected
**Solution:** Ensure wake word detection is enabled and microphone sensitivity is correctly configured.

### Issue: Incorrect voice command execution
**Solution:** Verify command sentences and adjust custom pipelines if necessary.

---

*Generated using AI*