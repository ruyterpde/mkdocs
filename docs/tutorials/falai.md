---
title: Interacting with fal.ai Public Functions
description: A comprehensive tutorial on programmatically accessing and utilizing fal.ai's pre-built public functions, such as AI models for image generation or language processing, using the fal-ai Python SDK.
authors:
  - Documentation Team
tags:
  - fal.ai
  - API
  - serverless
  - python
  - AI
  - tutorial
icon: material/api
---

# Interacting with fal.ai Public Functions

## 1. Introduction

Welcome to this tutorial on interacting with `fal.ai`'s public functions. `fal.ai` provides a powerful serverless platform designed for running AI models, particularly those requiring GPUs. Beyond deploying your custom functions, `fal.ai` offers a suite of pre-built, publicly accessible functions (often referred to as models) that you can readily integrate into your applications.

This guide will walk you through the process of leveraging these public functions programmatically using the `fal-ai` Python SDK, focusing on a practical example like generating images with Stable Diffusion.

## 2. Overview

Many developers and researchers require access to state-of-the-art AI models without the overhead of managing underlying GPU infrastructure, model deployment, or scaling. This is particularly true for resource-intensive tasks such as large language model inference or complex image generation.

`fal.ai` solves this problem by providing a streamlined API to invoke these models as serverless functions. You simply send inputs, and `fal.ai` handles the execution on optimized hardware, returning the outputs. This tutorial will demonstrate how to:

*   Set up your development environment.
*   Authenticate with the `fal.ai` platform.
*   Discover and call a public function using the `fal-ai` Python SDK.
*   Process the results from the function execution.

## 3. Prerequisites

Before you begin, ensure you have the following:

*   **Python 3.8 or newer**: You can download it from [python.org](https://www.python.org/downloads/).
*   **`pip`**: Python's package installer, usually bundled with Python installations.
*   **A `fal.ai` Account**:
    *   You can sign up for a free account at [fal.ai](https://www.fal.ai/). Basic usage often falls within the free tier.
*   **`fal.ai` API Key**:
    *   Once logged into your `fal.ai` dashboard, navigate to the "API Keys" section.
    *   Generate a new API key. This key grants programmatic access to your `fal.ai` resources. Treat it as sensitive information.

    !!! warning "Keep Your API Key Secure"
        Never expose your API key in client-side code, public repositories, or plain text in configuration files. Use environment variables or secure secret management services.

*   **Basic Command Line Knowledge**: Familiarity with executing commands in a terminal.
*   **Basic Python Knowledge**: Understanding of Python syntax, functions, and data structures.

## 4. Execution

Follow these steps to interact with a `fal.ai` public function. We'll use the Stable Diffusion `v1.5` text-to-image model as our example.

### Step 1: Install the `fal-ai` SDK

Open your terminal or command prompt and install the `fal-ai` Python SDK:

```bash
pip install fal_ai
```

### Step 2: Set Up Your `fal.ai` API Key

It is best practice to set your `fal.ai` API key as an environment variable. Replace `YOUR_FAL_KEY_HERE` with the actual key you obtained from your `fal.ai` dashboard.

**Linux / macOS:**

```bash
export FAL_KEY="YOUR_FAL_KEY_HERE"
```

**Windows (Command Prompt):**

```cmd
set FAL_KEY="YOUR_FAL_KEY_HERE"
```

**Windows (PowerShell):**

```powershell
$env:FAL_KEY="YOUR_FAL_KEY_HERE"
```

Alternatively, you can pass the key directly in your Python script, but this is less recommended for production environments:

```python
import fal_ai as fal
fal.FAL_KEY = "YOUR_FAL_KEY_HERE" # Not recommended for production
```

### Step 3: Choose a Public Function (Model ID)

`fal.ai` hosts numerous public models. You can find a list and their respective `model_id` values in the `fal.ai` documentation, for example, under their [Models section](https://docs.fal.ai/models/).

For this tutorial, we will use the Stable Diffusion `v1.5` model, which has the `model_id`: `fal-ai/stable-diffusion-v1-5`.

### Step 4: Write the Python Script

Create a new Python file (e.g., `generate_image.py`) and add the following code:

```python
import fal_ai as fal
import os
import requests

# Define the model ID for the Stable Diffusion v1.5 public function
# You can explore other public models in the fal.ai documentation.
MODEL_ID = "fal-ai/stable-diffusion-v1-5"

# Define the prompt for image generation
PROMPT = "a professional photograph of an astronaut riding a majestic horse on the moon, cinematic, 8k"

# Define output directory
OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"--- Calling fal.ai public function: {MODEL_ID} ---")
print(f"Prompt: {PROMPT}")

try:
    # Call the fal.run() method with the model ID and its specific arguments
    # The arguments dictionary varies per function. Refer to fal.ai docs for each model.
    result = fal.run(
        MODEL_ID,
        arguments={
            "prompt": PROMPT,
            "width": 768,
            "height": 512,
            "num_inference_steps": 50,
            "seed": 42, # A fixed seed for reproducibility
        },
    )

    # Check if images were returned
    if result and "images" in result and len(result["images"]) > 0:
        image_url = result["images"][0]["url"]
        image_filename = os.path.join(OUTPUT_DIR, "generated_image.png")

        print(f"\n--- Image generated successfully! ---")
        print(f"Image URL: {image_url}")

        # Download the image
        print(f"Downloading image to {image_filename}...")
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_filename, "wb") as f:
                f.write(response.content)
            print("Image saved successfully.")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    else:
        print("\n--- No images found in the result. ---")
        print(f"Full result: {result}")

except fal.FalServerlessError as e:
    print(f"\n--- An error occurred during function execution: ---")
    print(f"Error Type: {type(e).__name__}")
    print(f"Message: {e}")
    print(f"Details: {e.details}")
except Exception as e:
    print(f"\n--- An unexpected error occurred: ---")
    print(f"Error Type: {type(e).__name__}")
    print(f"Message: {e}")

```

#### Code Explanation:

*   `import fal_ai as fal`: Imports the `fal_ai` SDK.
*   `fal.run(MODEL_ID, arguments={...})`: This is the core function call.
    *   `MODEL_ID`: Specifies which `fal.ai` public function to execute.
    *   `arguments`: A dictionary of parameters required by the specific model. These parameters are unique to each model (e.g., `prompt`, `width`, `height` for image generation). Always refer to the model's specific documentation on `fal.ai` for required arguments.
*   The `result` object contains the output from the function, which for image generation includes a list of image URLs.
*   We use the `requests` library to download the generated image. You might need to `pip install requests` if you don't have it.

### Step 5: Run the Script

Save the file and run it from your terminal:

```bash
python generate_image.py
```

## 5. Validation

Upon successful execution, your terminal output should resemble the following:

```
--- Calling fal.ai public function: fal-ai/stable-diffusion-v1-5 ---
Prompt: a professional photograph of an astronaut riding a majestic horse on the moon, cinematic, 8k

--- Image generated successfully! ---
Image URL: https://media.fal.ai/path/to/your/generated_image.png
Downloading image to generated_images/generated_image.png...
Image saved successfully.
```

Additionally, you should find a new directory named `generated_images` in the same location as your script, containing a file named `generated_image.png`. Open this image file to verify the output from the Stable Diffusion model.

!!! tip "Troubleshooting"
    *   **Authentication Error**: If you see an error related to `FAL_KEY` or authentication, double-check that your `FAL_KEY` environment variable is correctly set and that the key itself is valid.
    *   **Argument Error**: If the model complains about missing or invalid arguments, cross-reference the `arguments` dictionary in your script with the official `fal.ai` documentation for the specific `MODEL_ID` you are using.
    *   **Network Issues**: Ensure you have an active internet connection.
    *   **Rate Limits**: If you are making many requests quickly, you might hit `fal.ai`'s rate limits. The SDK usually handles retries, but a brief pause might be needed.

## 6. Tearing Down

Since `fal.ai`'s public functions are serverless, there is no infrastructure for you to explicitly "tear down" or de-provision. However, you can clean up your local environment and manage your `fal.ai` account resources:

*   **Delete Generated Files**: Remove the `generated_images` directory and its contents:
    ```bash
    rm -rf generated_images  # Linux/macOS
    rmdir /s /q generated_images # Windows
    ```
*   **Delete Script**: Remove the `generate_image.py` file.
*   **Uninstall SDK (Optional)**: If you no longer plan to use `fal.ai`, you can uninstall the SDK:
    ```bash
    pip uninstall fal_ai requests
    ```
*   **Revoke API Key (Optional but Recommended)**: For security, if you no longer need the API key used for this tutorial, consider revoking it from your `fal.ai` dashboard. This prevents unauthorized use.

## 7. Conclusion

You have successfully learned how to interact with `fal.ai`'s powerful public functions using the `fal-ai` Python SDK. You can now:

*   Set up your development environment for `fal.ai` API calls.
*   Securely authenticate using your `fal.ai` API key.
*   Invoke pre-trained AI models like Stable Diffusion for tasks such as image generation.
*   Process and validate the results from `fal.ai` function executions.

This capability opens up a world of possibilities for integrating advanced AI into your applications without the complexities of infrastructure management. Explore the `fal.ai` documentation further to discover other public functions and learn about deploying your own custom serverless applications.

*   [fal.ai Official Documentation](https://docs.fal.ai/)
*   [fal.ai Models List](https://docs.fal.ai/models/)
```