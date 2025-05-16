---
Title: Whisper + Wyoming Installation Guide (Windows Server)
Summary: A step-by-step installation guide for OpenAI Whisper and Wyoming-Whisper on Windows Server.
Author:
  - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Whisper

## Overview
Whisper + Wyoming Installation Guide (Windows Server)

This guide helps you install [OpenAI Whisper](https://github.com/openai/whisper) and [Wyoming-Whisper](https://github.com/earlephilhower/wyoming-whisper) on a Windows Server so you can offload transcription for Home Assistant device or in my case if your CPU doesn't support AVX.

### Technical Details
- Windows Server or Windows 10/11
- Python 3.8+ (installed from https://www.python.org/)
- Admin rights on the machine

### Infobox
!!! succes
    Succesfully tested on Windows Server 2025.

### Steps

1. Use Correct Python
   Verify Python is installed:

   ```bash
   where python
   ```

   If the first result is something like:  

   C:\Users\Administrator\AppData\Local\Programs\Python\Python3xx\python.exe  

   You’re good. If you see msys64 or Git\usr\bin, reinstall Python from python.org and check "Add to PATH" during installation.

2. Create and Activate Virtual Environment
   Use the correct Python path explicitly:

   ```bash
   "C:\Program Files\Python\Python313\python.exe" -m venv whisper_env  
   ```

   ```bash
   whisper_env\Scripts\activate
   ```

   You should now see your prompt change to:

   (whisper_env) C:\Users\Administrator>

3. Install Whisper and Torch
   Install Whisper and PyTorch (use CPU if no GPU available):

   ```bash
   pip install git+https://github.com/openai/whisper.git
   ```

   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
   ```

<<<<<<< HEAD
   You can replace cpu with cu118 for CUDA 11.8 if you have a compatible NVIDIA GPU.
=======
    You can replace cpu with cu118 for CUDA 11.8 if you have a compatible NVIDIA GPU.
>>>>>>> 803483de19e089041654b9596233bb7b0444ac00

4. Install and Run Wyoming-Whisper
   Clone and install Wyoming-Whisper:

   ```bash
   git clone https://github.com/rhasspy/wyoming-faster-whisper.git
   ```

   ```bash
   cd wyoming-faster-whisper
   ```

   ```bash
   pip install -r requirements.txt
   ```

   Start Whispwer with:

   ```bash
   python -m wyoming_faster_whisper --model tiny-int8 --language en --uri tcp://0.0.0.0:10300 --data-dir .\data --download-dir .\data
   ```

   This starts the Wyoming server on port 10300. You can change the model if you like.

5. Connect to Home Assistant  
   In Home Assistant:

   In Home Assistant: Configure Wyoming Integration  
   Go to Home Assistant UI.  
   Go to Settings > Devices & Services > Add Integration  
   Search for Wyoming  
   Host: The local IP address of your Windows Server (e.g., 192.168.1.100)  
   Port: 10300 (or whatever port Wyoming-Whisper is using)  
   Click Submit.  

Use services.yaml (if manual setup is needed)
If you want to manually define the Wyoming STT (Speech-to-Text) service in your config files:

``` yaml
stt:
  - platform: wyoming
    name: Whisper STT
    host: 192.168.1.100  # Your Windows Server IP
    port: 10300
```

After editing the config, restart Home Assistant.
Change the Speech-to-text option in the Home Assistant > Voice Assistants settings to [faster-whisper]

6. (Optional): Test Whisper Locally
   Try running a quick transcription:

   ```bash
   whisper example.wav --model small
   ```

Auto-Start (Optional)
Create a .bat file with run command (nog aanpassen):

```bash
@echo off
REM Set working directory to where this .bat file is located
cd /d %~dp0

echo INFO:__open__
REM Activate the virtual environment
call whisper_env\Scripts\activate.bat

REM Change to wyoming-faster-whisper directory
cd wyoming-faster-whisper

REM Start the Wyoming Faster Whisper server using venv Python
python -m wyoming_faster_whisper ^
  --model tiny-int8 ^
  --language en ^
  --uri tcp://0.0.0.0:10300 ^
  --data-dir .\data ^
  --download-dir .\data

pause
```

Place this in Startup or use Task Scheduler to auto-start at boot.

## You're Done!
Whisper is now offloaded from your Home Assistant device to your more powerful Windows Server.


### New pip:
To update, run:

```
python.exe -m pip install --upgrade pip
```
___
### Firewall Settings
Run this in an elevated CMD to allow Home Assistant to reach port 10300:

```bash
<<<<<<< HEAD
netsh advfirewall firewall add rule name="Whisper Wyoming" dir=in action=allow protocol=TCP localport=10300 profile=private,domain

=======
netsh advfirewall firewall add rule name="Whisper Wyoming" dir=in action=allow protocol=TCP localport=10300
>>>>>>> 803483de19e089041654b9596233bb7b0444ac00
```

### Commands

``` cmd
@echo off
echo -----------------------------------
echo   Updating Wyoming Faster Whisper 
echo -----------------------------------

REM Navigate to base folder
cd /d %~dp0

REM Activate the virtual environment
call whisper_env\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Go into the wyoming-faster-whisper directory
cd wyoming-faster-whisper

REM Pull latest code (safe if not modified)
echo Pulling latest Wyoming Faster Whisper code...
git pull

REM Upgrade all dependencies
echo Upgrading Python dependencies...
pip install --upgrade -r requirements.txt

echo Update complete!
pause

```

### Examples
    Code snippets, commands, or use cases.

### Resources
    Links to related articles, external documentation, or downloadable tools.

### Troubleshooting
    Issues and resolutions.

<<<<<<< HEAD
### Choices
And to make it even more complex: [See my Docker CE adventure](../../Local_n8n/docker.md)
Plan is to run Whisper from a Docker Container

=======
>>>>>>> 803483de19e089041654b9596233bb7b0444ac00
---

*Generated using AI*    