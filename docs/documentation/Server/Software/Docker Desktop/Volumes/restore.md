docker run --rm \
  -v n8n_data:/data \
  -v $(pwd):/backup \
  alpine \
  sh -c "cd /data && tar xzvf /backup/n8n_data_backup.tar.gz"
