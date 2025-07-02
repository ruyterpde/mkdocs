```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <system.webServer>
    <!-- Enable WebSocket if permitted -->
    <webSocket enabled="true" />
    
    <!-- Reverse proxy logic to n8n -->
    <rewrite>
      <rules>
        <rule name="ReverseProxyToN8N" stopProcessing="true">
          <match url="(.*)" />
          <action type="Rewrite" url="http://localhost:5678/{R:1}" />
          <serverVariables>
            <set name="HTTP_UPGRADE" value="{HTTP_UPGRADE}" />
            <set name="HTTP_CONNECTION" value="{HTTP_CONNECTION}" />
            <set name="HTTP_X_FORWARDED_FOR" value="{REMOTE_ADDR}" />
            <set name="HTTP_X_FORWARDED_HOST" value="{HTTP_HOST}" />
            <set name="HTTP_X_FORWARDED_PROTO" value="https" />
          </serverVariables>
        </rule>
      </rules>
    </rewrite>

    <proxy>
      <reverseProxy enabled="true" />
    </proxy>
  </system.webServer>
</configuration>
```

In applicationHost.config:
```
notepad "$env:windir\System32\inetsrv\config\applicationHost.config"
```

```
<section name="webSocket" overrideModeDefault="Deny" />
to
<section name="webSocket" overrideModeDefault="Allow" />
```

In IIS on Site > URL Rewrite > View Server Variables and add:
"HTTP_X_FORWARDED_FOR"
"HTTP_X_FORWARDED_HOST"
"HTTP_X_FORWARDED_PROTO"
"HTTP_UPGRADE"
"HTTP_CONNECTION"

n8n-comfig.env:
# n8n basis settings
VUE_APP_URL=https://n8n.ruyter.org/
WEBHOOK_URL=https://n8n.ruyter.org/
N8N_HOST=n8n.ruyter.org
N8N_PORT=5678
N8N_PROTOCOL=https
N8N_EDITOR_BASE_URL=https://n8n.ruyter.org/
N8N_API_BASE_URL=https://n8n.ruyter.org/

# Belangrijk achter proxy
N8N_GENERIC_EXPRESS_CONFIG__TRUST_PROXY=1

# Optioneel: beveiligings- en permissie settings
N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=1

# Runners aanzetten indien nodig
N8N_RUNNERS_ENABLED=1