$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Add-Content -Path "$PSScriptRoot\Start-Stop_Docker_n8n.log" -Value "[$timestamp] n8n server starting..."

# Set working directory to the script's location
Set-Location -Path $PSScriptRoot

# Stop and remove existing container
docker stop n8n
docker rm n8n

# Generate timestamped backup filename
$backupDir = "C:\STORAGE\STORAGE.BACKUP\DOCKER_Volumes"
$backupTimestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupFile = "n8n_data_backup_$backupTimestamp.tar.gz"

# Create backup directory if it doesn't exist
if (-not (Test-Path $backupDir)) {
    New-Item -Path $backupDir -ItemType Directory | Out-Null
}

$containerCommand = "tar czvf /backup/$backupFile -C /data ."

# Create backup using temporary alpine container
docker run --rm `
    -v n8n_data:/data `
    -v "${backupDir}:/backup" `
    alpine `
    sh -c "$containerCommand"

# Update n8n image
docker pull n8nio/n8n:latest
docker pull alpine:latest

# Start container again
docker run -d `
  --name n8n `
  --restart unless-stopped `
  --env-file C:\Users\Administrator\.docker\n8n-config.env `
  -p 5678:5678 `
  -v n8n_data:/home/node/.n8n `
  n8nio/n8n:latest