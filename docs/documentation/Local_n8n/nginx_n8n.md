---
Title: Installation of NGINX and N8N in WSL Docker
Summary: A guide to installing and configuring NGINX and N8N on Docker within Windows Subsystem for Linux (WSL).
Author:
  - Peter de Ruyter
Date: 2025-05-12
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# NGINX n8n

## Installation of NGINX and N8N in WSL Docker

## Overview
This guide walks through the installation and setup of NGINX and N8N in WSL Docker to enable a streamlined development environment.

### Technical Details
NGINX is a high-performance web server and reverse proxy, while N8N is an automation tool enabling workflow integrations. Running both in Docker under WSL enhances portability and efficiency.

### Infobox
| Component  | Version | Purpose |
|------------|---------|---------|
| NGINX      | Latest  | Web Server |
| N8N        | Latest  | Workflow Automation |
| Docker     | Latest  | Container Management |
| WSL        | 2       | Linux Compatibility |

### Steps
#### 1. Install Docker in WSL
```sh
sudo apt update && sudo apt install docker.io
sudo systemctl enable --now docker
```

#### 2. Pull and Run NGINX Container
```sh
docker pull nginx
docker run -d -p 80:80 --name nginx-container nginx
```

#### 3. Pull and Run N8N Container
```sh
docker pull n8nio/n8n
docker run -d -p 5678:5678 --name n8n-container n8nio/n8n
```

#### 4. Configure NGINX as a Reverse Proxy
Create an NGINX configuration file:
```sh
nano /etc/nginx/conf.d/n8n.conf
```
Add the following content:
```nginx
server {
    listen 80;
    server_name n8n.local;

    location / {
        proxy_pass http://localhost:5678;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
Then restart NGINX:
```sh
docker exec nginx-container nginx -s reload
```

### Commands
Common Docker commands for managing containers:
```sh
docker ps          # List running containers
docker stop nginx-container n8n-container  # Stop containers
docker start nginx-container n8n-container # Start containers
docker logs nginx-container  # View logs
```

### Examples
Running N8N workflows:
```sh
docker exec -it n8n-container n8n
```

### Resources
- [NGINX Official Docs](https://nginx.org/en/docs/)
- [N8N Documentation](https://docs.n8n.io/)
- [Docker in WSL Guide](https://docs.microsoft.com/en-us/windows/wsl/docker)

### Troubleshooting
#### Issue: NGINX Not Starting
Check logs:
```sh
docker logs nginx-container
```
Verify configuration:
```sh
nginx -t
```

#### Issue: N8N Port Not Accessible
Ensure the container is running:
```sh
docker ps | grep n8n
```
Restart the container:
```sh
docker restart n8n-container
```

---

*Generated using AI*