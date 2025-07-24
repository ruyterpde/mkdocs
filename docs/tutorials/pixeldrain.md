---
title: PixelDarin API Tutorial
description: Learn how to use the CloudConvert API to convert files programmatically using MkDocs-Material compatible Markdown.
tags:
  - cloudconvert
  - api
  - file-conversion
  - tutorial
---

# Introduction

This tutorial provides a structured guide to using the **PixelDrain API**, a lightweight and fast file-sharing service. You'll learn how to upload, retrieve, and manage files programmatically using HTTP requests.

# Overview

The PixelDrain API allows developers to:
- Upload files and receive shareable links
- Retrieve file metadata and thumbnails
- Download or delete files
- Organize files into lists

This tutorial solves the problem of integrating file-sharing capabilities into your application without relying on heavy third-party services.

# Prerequisites

Before you begin, ensure you have:
- A PixelDrain account (for API key access)
- Basic knowledge of HTTP requests and command-line tools
- `curl` or any HTTP client (e.g., Postman, Python `requests`)
- Your API key from [PixelDrain API Keys](https://pixeldrain.com/api)

# Execution

## 1. Upload a File

<<<sh
curl -X PUT -u :<YOUR_API_KEY> https://pixeldrain.com/api/file/ -T path/to/file.txt

## 2. Get File Info

<<<sh
curl -X GET -u :<YOUR_API_KEY> https://pixeldrain.com/api/file/<FILE_ID>/info

## 3. Download a File

<<<sh
curl -X GET -u :<YOUR_API_KEY> https://pixeldrain.com/api/file/<FILE_ID> --output downloaded.txt

## 4. Delete a File

<<<sh
curl -X DELETE -u :<YOUR_API_KEY> https://pixeldrain.com/api/file/<FILE_ID>

## 5. Create a File List

<<<json
{
  "title": "My File List",
  "anonymous": false,
  "files": [
    { "id": "abc123", "description": "First file" },
    { "id": "def456", "description": "Second file" }
  ]
}

<<<sh
curl -X POST -u :<YOUR_API_KEY> https://pixeldrain.com/api/list -H "Content-Type: application/json" -d @list.json

# Validation

To verify success:
- Check the response JSON for `"success": true`
- Visit `https://pixeldrain.com/u/<FILE_ID>` to preview the file
- Use the `/info` endpoint to confirm metadata like size, views, and MIME type

# Tearing Down

To clean up:
- Use the DELETE endpoint to remove files
- Remove lists using the `/user/lists` interface (requires authentication)
- Revoke your API key if no longer needed

# Conclusion

You've now mastered the basics of the PixelDrain API:
- Uploading and managing files
- Retrieving metadata and thumbnails
- Organizing files into lists

For advanced usage and error handling, refer to the [official PixelDrain API documentation](https://pixeldrain.com/api). Happy sharing!

---

*Generated using AI*