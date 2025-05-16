---
Title: Installation of Node.js on Windows
Summary: A comprehensive guide to installing Node.js on Windows using MkDocs-Material.
Author:
  - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

## Installation

## Node.js Installation
Installing Node.js on Windows

## Overview
Node.js is an open-source, cross-platform JavaScript runtime environment that allows developers to build scalable network applications. This guide provides step-by-step instructions for installing Node.js on Windows.

### Technical Details
Node.js can be installed on Windows using the official installer or a package manager such as Chocolatey or Scoop. The recommended approach is to download the installer directly from the official Node.js website.

### Infobox
| Tool | Description |
|------|------------|
| Node.js | JavaScript runtime built on Chrome's V8 engine |
| npm | Default package manager for Node.js |
| Chocolatey | Windows package manager for automated installations |
| Scoop | Lightweight package manager for Windows |

### Steps
#### Download and Install Node.js
1. Visit the [Official Node.js website](https://nodejs.org/en).
2. Choose the recommended version for Windows.
3. Download the installer (`.msi` file).
4. Run the installer and follow the setup wizard instructions.
5. Verify the installation using the command:

```sh
node -v
```

#### Install via Chocolatey
If Chocolatey is installed, use:

```sh
choco install nodejs
```

#### Install via Scoop
For Scoop users:

```sh
scoop install nodejs
```

### Install Additional Tools for Node.js
This script will install Python and the Visual Studio Build Tools, necessary to compile Node.js native modules. Note that Chocolatey and required Windows updates will also be installed. This will require about 3 GiB of free disk space, plus any space necessary to install Windows updates. This will take a while to run. Please close all open programs for the duration of the installation. If the installation fails, please ensure Windows is fully updated, reboot your computer and try to run this again. This script can be found in the Start menu under Node.js. Detailed instructions to install these tools manually are available at [Tools for Node.js](https://github.com/nodejs/node-gyp#on-windows).

This script will direct to Chocolatey to install packages. By using Chocolatey to install a package, you are accepting the license for the application, executable(s), or other artifacts delivered to your machine as a result of a Chocolatey install. This acceptance occurs whether you know the license terms or not. Read and understand the license terms of the packages being installed and their dependencies prior to installation:

- https://chocolatey.org/packages/chocolatey
- https://chocolatey.org/packages/python
- https://chocolatey.org/packages/visualstudio2019-workload-vctools

This script is provided AS-IS without any warranties of any kind.

```bash
"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" ^
-NoProfile ^
-InputFormat None ^
-ExecutionPolicy Bypass ^
-Command Start-Process ^
    '%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe' ^
    -ArgumentList '-NoProfile -InputFormat None -ExecutionPolicy Bypass -Command ^
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; ^
    iex ((New-Object System.Net.WebClient).DownloadString(''https://chocolatey.org/install.ps1'')); ^
    choco upgrade -y python visualstudio2019-workload-vctools; ^
    Read-Host ''Type ENTER to exit'' ' ^
    -Verb RunAs
```

### Install n8n
Open your command-line interface (CLI) and execute the command:

```bash
npm install n8n -g
```

This installs n8n globally on your machine, making it accessible from any directory.

### Your done
Launch n8n by typing n8n or n8n start in the CLI.  
This command starts the platform locally, allowing you to access it through your web browser.

```bash
n8n start
```

Once n8n is running, open your browser and navigate to the local address provided in the CLI. During the initial setup, you’ll be prompted to create an admin account by entering your email address, name, and password. This account will serve as your primary access point for managing workflows and configurations.

### How to update n8n
Keeping n8n updated is essential to take advantage of the latest features, performance enhancements, and security updates. Updating the platform is simple and can be done using the following command in your CLI:

```bash
npm update -g n8n
```

It is recommended to check for updates regularly to ensure compatibility with external services and maintain optimal performance. Staying up-to-date also helps you avoid potential issues caused by outdated dependencies or integrations.



### Commands
| Command | Description |
|---------|------------|
| `node -v` | Check installed Node.js version |
| `npm -v` | Check installed npm version |
| `npm install -g <package>` | Install a global Node.js package |

### Examples
#### Running a Simple Node.js Script
Create a `hello.js` file:

```js
console.log("Hello, Node.js!");
```

Run the script:

```sh
node hello.js
```

### Resources
- [Node.js Official Documentation](https://nodejs.org/en/docs/)
- [Chocolatey Node.js Package](https://community.chocolatey.org/packages/nodejs)
- [Scoop Node.js Package](https://scoop.sh/)
- [Hosting n8n](https://docs.n8n.io/hosting/)
- [Community Edition n8n](https://docs.n8n.io/hosting/community-edition-features/)

### Troubleshooting
#### Path Issues
Ensure Node.js is added to the system `PATH`:

```sh
echo %PATH%
```

#### Permission Errors
Run the installer as administrator or use:

```sh
npm config set prefix %USERPROFILE%\npm
```

### Choices
And to make it even more complex: [See my Docker CE adventure](docker.md)

---

*Generated using AI*