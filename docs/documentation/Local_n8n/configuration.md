---
Title: Configuration of Local Installed n8n Environment
Summary: Guide to setting up and configuring an n8n environment locally.
Author:
  - Peter de Ruyter
Date: 2025-05-08
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Configuration

## Configuration of Local Installed n8n Environment
Setting up an n8n instance locally with network access and security considerations.

## Overview
This document provides a detailed guide for configuring an n8n environment installed on a local machine. It includes steps for enabling network access and setting up TLS/HTTPS for secure connections.

### Technical Details
This section dives deep into the configuration settings for a locally installed n8n environment.

### Infobox
| Feature        | Description |
|---------------|-------------|
| Host Config   | Allows access from other devices on the network |
| TLS/HTTPS     | Secures connections with encryption |

### Steps
#### Configuring Host for Network Access
1. Modify the `.env` file to set the host:
   ```env title=sample
   WEBHOOK_URL=https://your-local-ip:5678
   N8N_HOST=your-local-ip
   N8N_PORT=5678
   ```

   ```env title=sample
   N8N_HOST=0.0.0.0
   N8N_PORT=5678
   N8N_PROTOCOL=http
   SSL_CERT_PATH=cert.pem
   SSL_KEY_PATH=key.pem
   ```

Store this file in the root of the n8n installation. In my case:
```
C:\Users\username\AppData\Roaming\npm
```

2. Restart the n8n service:
   ```sh
   pm2 restart n8n
   ```

#### Setting Up TLS/HTTPS
1. Generate SSL certificates using Let's Encrypt or OpenSSL.
2. Configure n8n to use SSL:
   ```env
   N8N_PROTOCOL=https
   SSL_CERT_PATH=/path/to/fullchain.pem
   SSL_KEY_PATH=/path/to/privkey.pem
   ```

3. Restart n8n to apply changes.

### Commands
| Command                | Description |
|------------------------|-------------|
| `pm2 restart n8n`      | Restarts the n8n service |
| `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes` | Generates a self-signed SSL certificate |

### Examples
#### Sample Reverse Proxy Configuration (NGINX)
```conf
server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    location / {
        proxy_pass http://localhost:5678;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Resources
- [n8n Documentation](https://docs.n8n.io/)
- [Let's Encrypt Guide](https://letsencrypt.org/)
- [NGINX Reverse Proxy Setup](https://nginx.org/en/docs/)

### Troubleshooting
#### Issue: Unable to Access from Other Devices
**Solution:** Ensure firewall settings allow connections on the specified port.

#### Issue: SSL Not Working
**Solution:** Verify the certificate paths and permissions.

---

*Generated using AI*