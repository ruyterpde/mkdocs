---
Title: Installation of LLM Local AI on Windows
Summary: A comprehensive guide to installing a lightweight local language model (LLM) on Windows.
Author:
  - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Installation

## Installation of LLM Local AI on Windows
Guidelines for setting up a small, local Language Model (LLM) using Ollama or llama.cpp.

## Overview
This guide provides step-by-step instructions for installing a local and lightweight Language Model (LLM) on Windows. The recommended tools include Ollama and llama.cpp, with compact models such as Mistral, TinyLlama, and Gemma:2b.

### Technical Details
- **Model Options**: Mistral, TinyLlama, Gemma:2b
- **Tool Used**: Ollama
- **Execution Method**: Simple CLI (`ollama run mistral`)
- **Hardware Requirements**: Runs on CPU or GPU
- **Customization**: Fine-tuning and prompt engineering options available

### Infobox
| Feature            | Details                         |
| ----------------   |-------------------------------- |
| Model Types        | Mistral, TinyLlama, Gemma:2b    |
| Tool Used          | Ollama                          |
| Execution          | CLI: `ollama run mistral`       |
| Supported Hardware | CPU, GPU                        |
| Customization      | Fine-tuning, prompt engineering |

### Steps

1. **Install Python**  
    Download and install Python 3.10+  
    During installation: check the box "Add Python to PATH"  

    ```bash
        python --version
    ```

2. **Install pip dependencies**  
    Open a terminal (CMD or PowerShell) and run  

    ```bash
    pip install flask experta requests
    ```

3. **Install Waitress**  
    Open a terminal (CMD or PowerShell) and run  

    ```bash
    pip install waitress
    ```

    Waitress is a production-ready WSGI server for Python, as an alternative to Flask's own development server.

4. **Install and Run Ollama on Windows**  
    Ollama now offers a Windows-native version. Visit the official Ollama website and download the latest version.  
    Go to: [ollama.com/download](https://ollama.com/download)  
    Install the Windows version.

5. **Run a model locally**  
    After installation, in a new terminal  
    
    ```bash
    ollama run mistral
    ```

    The first time, it will download the model (~4-7 GB).  
    Your language model will now run locally via http://localhost:11434

6. **Run the Script**  
    A sample script is available [offline_assistent.py](offline_assistant.md). Make sure you have saved this script locally, e.g., as offline_assistent.py  
    Start the script via CMD or PowerShell  

    ```bash
    python offline_assistent.py
    ```

7. **Test your installation**
    Then visit in your browser >

    http://localhost:5000

8. **Fine-tune or customize**  
    Modify prompts or parameters as needed to optimize model performance.

### Commands
Commonly used commands for installing and running the model:
```
ollama pull mistral
ollama run mistral
```

### Examples
Example usage of the installed model:
```
ollama run tinyllama
```

### Resources
- [Ollama Official Documentation](https://ollama.ai)
- [MkDocs-Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Llama.cpp Repository](https://github.com/ggerganov/llama.cpp)

### Troubleshooting
| Issue              | Resolution                                          |
| ------------------ | --------------------------------------------------- |
| Installation fails | Ensure Ollama is properly downloaded and installed  |
| Model not found    | Verify the model name and run `ollama pull <model>` |
| Performance issues | Adjust settings or run on GPU for optimization      |

---

*Generated using AI*