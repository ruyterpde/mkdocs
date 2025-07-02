docker run --rm \
  -v n8n_data:/data \
  -v $(pwd):/backup \
  alpine \
  tar czvf /backup/n8n_data_backup.tar.gz -C /data .
