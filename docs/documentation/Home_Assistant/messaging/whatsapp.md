---
Title: "How to Send WhatsApp Messages in Home Assistant"
Summary: "A guide to integrating WhatsApp messaging into Home Assistant using Call Me Bot."
Author:
  - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# WhatsApp

## How to Send WhatsApp Messages in Home Assistant

## Introduction  
Home Assistant is an open-source home automation platform that allows you to integrate various smart devices and services. One useful feature is the ability to send WhatsApp messages directly from Home Assistant. This guide will walk you through how to set up and use Call Me Bot for sending personal WhatsApp messages.  

## Prerequisites  
Before starting, ensure you have the following:  
- A working Home Assistant installation  
- An internet connection  
- A WhatsApp account  
- Access to Call Me Bot ([CallMeBot Website](https://www.callmebot.com/){:target="_blank"})  

## Step-by-Step Guide  

### Step 1: Request API Access  
1. Visit the Call Me Bot website.  
2. Follow the instructions to request access to their WhatsApp API.  
3. Once approved, you will receive a unique API key.  

### Step 2: Configure Home Assistant  
Edit your `configuration.yaml` file to include the following automation for sending messages:  

```yaml  
notify:  
  - name: whatsapp  
    platform: rest  
    resource: https://api.callmebot.com/whatsapp.php
    data:
      source: HA
      phone: YOUR_PHONE
      apikey: YOUR_APIKEY  
```  

Replace `YOUR_PHONE` and `YOUR_APIKEY` with your actual phone number and API key from Call Me Bot.  

### Step 3: Test the Integration  
To verify that your WhatsApp message automation is working, create a script in Home Assistant:  

```yaml  
script:  
  send_whatsapp_message:  
    alias: Send WhatsApp Message  
    sequence:  
      - service: notify.whatsapp  
        data:  
          message: "Hello from Home Assistant!"  
```  

Trigger the script from Home Assistant’s UI or through an automation. If correctly set up, you should receive a WhatsApp message.  

## Troubleshooting  
If you encounter issues, consider the following:  
- Ensure that your API key and phone number are correctly formatted.  
- Verify that Call Me Bot is operational by checking their website.  
- Check Home Assistant logs for any error messages related to the notification service.  

## Conclusion  
With this setup, you can automate personal WhatsApp messaging within Home Assistant using Call Me Bot, enabling better notifications and smart integrations for your home automation needs.

---

*Generated using AI*    
