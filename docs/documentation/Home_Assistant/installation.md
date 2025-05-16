---
Title: Installation of Home Assistant on Legacy Hardware x64 without UEFI BIOS
Summary: A comprehensive guide to installing Home Assistant on legacy x64 hardware that lacks UEFI BIOS support.
Author:
  - Peter de Ruyter
Date: 2025-05-05
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Installation

## Installation of Home Assistant on Legacy Hardware x64 without UEFI BIOS

## Overview
This guide provides step-by-step instructions for installing Home Assistant on legacy x64 hardware that does not support UEFI BIOS. It covers the preparation of bootable media, BIOS configuration, and installation of the Home Assistant Operating System (HAOS).

### Technical Details
- **Hardware Requirements**:
  - x64 architecture
  - Legacy BIOS (non-UEFI)
  - Minimum 2 GB RAM and 32 GB storage
- **Software Requirements**:
  - Home Assistant Operating System (HAOS) image
  - Rufus for creating bootable media
- **Outcome**: A fully functional Home Assistant instance running on legacy hardware.

### Infobox
**Key Facts**:
- **Platform**: Legacy x64 hardware
- **Boot Mode**: Legacy BIOS
- **Use Case**: Home automation on older hardware
- **Tools**: Rufus, HAOS image

---

## Steps

### 1. Download the Home Assistant Operating System Image
1. Visit the [Home Assistant Downloads](https://www.home-assistant.io/installation/) page.
2. Select the appropriate image for your hardware (e.g., x64 Generic).
3. Download the `.img.xz` file to your computer.

### 2. Prepare Bootable Media
1. Insert a USB drive (minimum 8 GB) into your computer.
2. Use a tool like Balena Etcher or Rufus to create bootable media:
   - **Rufus**:
     1. Open Rufus.
     2. Select the USB drive.
     3. Choose the downloaded `.img.xz` file.
     4. Set the partition scheme to "MBR" for legacy BIOS.
     5. Click "Start" to create the bootable media.

### 3. Configure BIOS Settings
1. Restart your computer and enter the BIOS setup (usually by pressing `DEL`, `F2`, or `F12` during boot).
2. Ensure the following settings are configured:
   - **Boot Mode**: Legacy BIOS
   - **Secure Boot**: Disabled
   - **Boot Priority**: Set the USB drive as the first boot device.
3. Save changes and exit the BIOS.

### 4. Install Home Assistant Operating System
1. Insert the bootable USB drive into the target hardware.
2. Power on the hardware and boot from the USB drive.
3. Follow the on-screen instructions to install HAOS on the internal storage.
4. Once the installation is complete, the system will reboot automatically.

### 5. Access Home Assistant
1. Connect the hardware to your network via Ethernet or Wi-Fi.
2. Open a web browser on a device connected to the same network.
3. Navigate to `http://homeassistant.local:8123` or the IP address assigned to the device.
4. Complete the initial setup wizard to configure your Home Assistant instance.

---

## Examples

### BIOS Configuration Example
- **Boot Mode**: Legacy
- **Secure Boot**: Disabled
- **Boot Priority**: USB Drive > Hard Disk

### YAML Configuration for Static IP
```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: false
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```
{: .code-copy}

---

## Resources
- [Home Assistant Installation Guide](https://www.home-assistant.io/installation/)
- [Rufus](https://rufus.ie/)
- [Home Assistant Networking](https://www.home-assistant.io/docs/network/)
- [Generic x86-64](https://www.home-assistant.io/installation/generic-x86-64)

---

## Troubleshooting

### Issue: USB Drive Not Detected in BIOS
**Resolution**: Ensure the USB drive is properly formatted and inserted. Try a different USB port or recreate the bootable media.

### Issue: Unable to Access Home Assistant Web Interface
**Resolution**: Verify the device is connected to the network. Check the IP address assigned to the device and use it to access the interface.

### Issue: Installation Fails on Legacy Hardware
**Resolution**: Confirm that the hardware meets the minimum requirements. Check the BIOS settings for compatibility with HAOS.

### Issue: Installation Fails to boot
[OS 15.x fails to boot on certain SATA drives](https://github.com/home-assistant/operating-system/issues/3948#issuecomment-2770837367)  

![bootloader](../../assets/images/bootloader_fix.png)

**Resolution**: Change boot loader after installation.
[Install HAOS without UEFI](https://www.reddit.com/r/homeassistant/comments/1d7fy79/you_dont_need_uefi_to_install_haos_heres_a_simple/)

---

*Generated using AI*