---
title: Interacting with the Pixeldrain Public API
authors:
  - Documentation Assistant
tags:
  - API
  - Pixeldrain
  - File Management
  - Upload
  - Download
  - Automation
icon: material/api
---

# Interacting with the Pixeldrain Public API

This tutorial provides a comprehensive guide on how to interact with the Pixeldrain public API using common programming concepts. You will learn to upload files, retrieve file information, download files, and manage uploaded content programmatically.

## Introduction

Pixeldrain is a versatile online service for sharing files. While its web interface offers a convenient way to upload and download content, its public API unlocks powerful capabilities for developers and users who wish to automate file management tasks. This guide will walk you through the essential API endpoints, enabling you to integrate Pixeldrain functionality directly into your applications or scripts.

## Overview

The primary challenge this tutorial addresses is the need for programmatic interaction with a file-sharing service. Manually uploading or downloading numerous files through a web browser can be time-consuming and inefficient. By leveraging the Pixeldrain API, users can:

- **Automate file uploads** from scripts or applications.
- **Retrieve detailed information** about uploaded files without manual inspection.
- **Programmatically download** files for processing or archiving.
- **Manage uploaded content** through deletion commands.

This tutorial focuses on the fundamental public API endpoints, providing a solid foundation for more complex integrations.

## Prerequisites

Before you begin, ensure you have the following:

- **Basic understanding of HTTP requests**: Familiarity with concepts like GET, POST, and DELETE methods.
- **A programming environment**: This tutorial will use Python for its simplicity and widespread adoption, along with the `requests` library for making HTTP calls.
- **`pip`**: Python's package installer, used to install the `requests` library.
- **An internet connection**: To access the Pixeldrain API.
- **`curl` (optional)**: Useful for quick tests and direct API calls from the command line.

To install the `requests` library, open your terminal or command prompt and run:

```bash
pip install requests
```

## Execution

This section details the step-by-step process of interacting with the Pixeldrain API.

### Step 1: Uploading a File

The most common operation is uploading a file. Pixeldrain allows anonymous uploads, which are ideal for quick sharing.

**API Endpoint:** `POST https://pixeldrain.com/api/file`
**Method:** `POST`
**Parameters:**
- `file`: The file data to upload.
- `anonymous` (optional): Set to `true` to perform an anonymous upload.

Let's create a dummy file for upload:

```bash
echo "This is a test file for the Pixeldrain API tutorial." > my_test_file.txt
```

Now, upload it using Python:

```python
import requests
import json

file_path = 'my_test_file.txt'

try:
    with open(file_path, 'rb') as f:
        files = {'file': f}
        data = {'anonymous': 'true'} # Optional: upload anonymously

        print(f"Uploading {file_path}...")
        response = requests.post('https://pixeldrain.com/api/file', files=files, data=data)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

        upload_info = response.json()
        
        file_id = upload_info.get('id')
        delete_key = upload_info.get('deleteKey') # Important for deletion!
        
        if file_id:
            print(f"File uploaded successfully!")
            print(f"File ID: {file_id}")
            print(f"Delete Key: {delete_key}")
            print(f"View URL: https://pixeldrain.com/u/{file_id}")
            print(f"Download URL: https://pixeldrain.com/api/file/{file_id}")
            
            # Save info for later steps
            with open('uploaded_file_info.json', 'w') as info_file:
                json.dump(upload_info, info_file, indent=4)
            print("File ID and Delete Key saved to 'uploaded_file_info.json'")
        else:
            print("Upload successful, but 'id' not found in response.")
            print(f"Response: {json.dumps(upload_info, indent=4)}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred during upload: {e}")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
```

!!! note
    The `deleteKey` is crucial if you intend to programmatically delete the file later. Always store it securely if needed. For anonymous uploads without an account, this is the only way to delete the file.

### Step 2: Getting File Information

Once a file is uploaded, you can retrieve its metadata.

**API Endpoint:** `GET https://pixeldrain.com/api/file/{id}/info`
**Method:** `GET`
**Parameters:** `{id}` - The ID of the uploaded file.

Let's use the `file_id` obtained from the previous step:

```python
import requests
import json

# Load file info saved from the upload step
try:
    with open('uploaded_file_info.json', 'r') as f:
        uploaded_file_info = json.load(f)
        file_id = uploaded_file_info.get('id')
    
    if not file_id:
        print("Error: 'file_id' not found in 'uploaded_file_info.json'. Please run the upload step first.")
        exit()

except FileNotFoundError:
    print("Error: 'uploaded_file_info.json' not found. Please run the upload step first.")
    exit()

try:
    print(f"\nRetrieving info for File ID: {file_id}...")
    response = requests.get(f'https://pixeldrain.com/api/file/{file_id}/info')
    response.raise_for_status()

    file_info = response.json()
    print("File Information:")
    print(json.dumps(file_info, indent=4))

except requests.exceptions.RequestException as e:
    print(f"An error occurred while retrieving file info: {e}")
    if response.status_code == 404:
        print("Error: File not found. It might have been deleted or the ID is incorrect.")
```

### Step 3: Downloading a File

You can directly download the content of an uploaded file.

**API Endpoint:** `GET https://pixeldrain.com/api/file/{id}`
**Method:** `GET`
**Parameters:** `{id}` - The ID of the file to download.

Let's download the `my_test_file.txt` we uploaded:

```python
import requests
import json
import os

# Load file info
try:
    with open('uploaded_file_info.json', 'r') as f:
        uploaded_file_info = json.load(f)
        file_id = uploaded_file_info.get('id')
        original_filename = uploaded_file_info.get('name', 'downloaded_file.txt') # Use original name or default
    
    if not file_id:
        print("Error: 'file_id' not found in 'uploaded_file_info.json'. Please run the upload step first.")
        exit()

except FileNotFoundError:
    print("Error: 'uploaded_file_info.json' not found. Please run the upload step first.")
    exit()

download_path = f"downloaded_{original_filename}"

try:
    print(f"\nDownloading File ID: {file_id} to {download_path}...")
    response = requests.get(f'https://pixeldrain.com/api/file/{file_id}', stream=True)
    response.raise_for_status()

    with open(download_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    print(f"File downloaded successfully to: {os.path.abspath(download_path)}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while downloading the file: {e}")
    if response.status_code == 404:
        print("Error: File not found. It might have been deleted or the ID is incorrect.")
```

### Step 4: Deleting a File

To clean up or manage storage, you can delete uploaded files. This requires the `deleteKey` obtained during the upload.

**API Endpoint:** `DELETE https://pixeldrain.com/api/file/{id}`
**Method:** `DELETE`
**Parameters:**
- `{id}`: The ID of the file to delete.
- `key`: The `deleteKey` associated with the file.

```python
import requests
import json
import os

# Load file info
try:
    with open('uploaded_file_info.json', 'r') as f:
        uploaded_file_info = json.load(f)
        file_id = uploaded_file_info.get('id')
        delete_key = uploaded_file_info.get('deleteKey')
    
    if not file_id or not delete_key:
        print("Error: 'file_id' or 'deleteKey' not found in 'uploaded_file_info.json'. Please run the upload step first.")
        exit()

except FileNotFoundError:
    print("Error: 'uploaded_file_info.json' not found. Please run the upload step first.")
    exit()

try:
    print(f"\nAttempting to delete File ID: {file_id}...")
    
    # Send the delete key as a query parameter
    response = requests.delete(f'https://pixeldrain.com/api/file/{file_id}?key={delete_key}')
    response.raise_for_status()

    delete_status = response.json()
    if delete_status.get('success'):
        print(f"File ID {file_id} deleted successfully.")
    else:
        print(f"Failed to delete file. Response: {json.dumps(delete_status, indent=4)}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred during file deletion: {e}")
    if response.status_code == 404:
        print("Error: File not found (already deleted or incorrect ID/key).")
    elif response.status_code == 401:
        print("Error: Unauthorized. The delete key might be incorrect or expired.")

# Remove the temporary info file
if os.path.exists('uploaded_file_info.json'):
    os.remove('uploaded_file_info.json')
    print("Removed 'uploaded_file_info.json'")
```

## Validation

To verify the tutorial's outcome, perform the following checks:

1.  **After Upload:**
    *   Confirm that the Python script outputs a `File ID` and `Delete Key`.
    *   Visit the `View URL` (e.g., `https://pixeldrain.com/u/{file_id}`) in your web browser. You should see the uploaded file content or a file information page.
2.  **After Getting File Information:**
    *   Verify that the script prints a JSON output containing details like `id`, `name`, `size`, `uploadDate`, etc., matching your expectations for the uploaded file.
3.  **After Downloading File:**
    *   Check your local directory for a new file named `downloaded_my_test_file.txt` (or whatever your `original_filename` was).
    *   Open this file and confirm its content matches the original `my_test_file.txt`.
    *   Compare the file sizes to ensure a complete download.
4.  **After Deleting File:**
    *   Re-attempt to visit the `View URL` (`https://pixeldrain.com/u/{file_id}`) in your web browser. You should now see a "404 Not Found" page or an error indicating the file does not exist.
    *   Re-run the "Getting File Information" script. It should now report a "404 Not Found" error, confirming the file's deletion from Pixeldrain.

## Tearing Down

To clean up resources and your local environment:

1.  **Delete Local Files:** Remove the temporary files created during the tutorial:
    *   `my_test_file.txt` (the original file uploaded)
    *   `downloaded_my_test_file.txt` (the file downloaded)

    You can do this manually or use a command like:
    ```bash
    rm my_test_file.txt downloaded_my_test_file.txt
    ```
    (On Windows, use `del my_test_file.txt downloaded_my_test_file.txt`)

2.  **Pixeldrain Files:** The "Deleting a File" step explicitly removed the uploaded file from Pixeldrain using its `deleteKey`. If you skipped that step, ensure you manually delete any files you don't wish to keep on Pixeldrain, especially if they are not anonymous or contain sensitive information. For anonymous uploads without an account, the `deleteKey` is the only way to delete the file programmatically.

## Conclusion

This tutorial has guided you through the fundamental interactions with the Pixeldrain public API, covering file uploads, information retrieval, downloads, and deletions. You have learned how to use Python's `requests` library to send HTTP requests, handle responses, and manage temporary data crucial for API operations.

By mastering these basic operations, you are now equipped to:

-   Automate routine file sharing tasks.
-   Integrate Pixeldrain functionality into larger scripts or applications.
-   Efficiently manage digital assets without relying solely on the web interface.

Remember to consult the official Pixeldrain API documentation for more advanced features, such as folder management, user-specific operations (if authenticated), and additional parameters for existing endpoints. The principles learned here are transferable to many other RESTful APIs.