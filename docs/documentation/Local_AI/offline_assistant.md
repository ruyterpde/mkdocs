---
Title: Simple Offline AI Assistant
Summary: A Python-based AI assistant that integrates an LLM and rule-based logic system.
Author:
  - Peter de Ruyter
Date: 2025-05-06
URL: https://dms.ruyter.org / https://ruyterpde.github.io/mkdocs
---

# Offline Assistant

## Simple Offline AI Assistant

## Overview
This project provides a sample Python-based AI assistant that operates offline. It integrates a language model and a rule-based system to simulate conversational AI while allowing extensions via a web interface.

### Technical Details
- **Language Model Simulation:** Processes user input via `parse_user_input`.
- **Rule-Based System:** Uses `Experta` for logical inference.
- **LLM Integration:** Utilizes `Ollama` for enhanced AI responses.
- **Web Interface:** Extendable for interaction beyond CLI.

### Infobox
| Feature | Description |
|---------|------------|
| Language Model | Simulates conversation via parsing logic |
| Rule System | Implements logical inference with `Experta` |
| LLM Integration | Uses `Ollama` to enhance AI capabilities |
| Web Interface | Extensible for broader access |

### Steps
Not applicable.

### Commands

```bash
python offline_assistent.py
```

### Examples

``` py title="offline_assistent.py" linenums="1"

from experta import *
from flask import Flask, request, jsonify, render_template_string
import subprocess
import requests
import json

# ---------------------------
# Regelgebaseerde AI
# ---------------------------
class SmartAssistant(KnowledgeEngine):

    @Rule(Fact(intent='turn_off_lights'), Fact(location='not_home'))
    def turn_off_lights(self):
        print("[Actie] Lichten worden uitgezet.")

    @Rule(Fact(intent='turn_on_heater'), Fact(temperature='cold'))
    def turn_on_heater(self):
        print("[Actie] Verwarming wordt aangezet.")


# ---------------------------
# Simpele LLM-integratie via Ollama
# ---------------------------
def call_llm(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        result = response.json()
        return result.get("response", "")
    else:
        return ""


def parse_llm_response(response):
    """
    Simpele parser: verwacht JSON-achtige output van de LLM zoals:
    {'intent': 'turn_off_lights'}
    """
    try:
        return json.loads(response)
    except:
        return {}


# ---------------------------
# Flask Webinterface
# ---------------------------
app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>Offline AI Assistent</title></head>
<body style="font-family: sans-serif; padding: 20px;">
    <h2>Offline AI Assistent</h2>
    <form method="post">
        <input type="text" name="user_input" placeholder="Typ je opdracht..." style="width: 300px;" />
        <button type="submit">Verstuur</button>
    </form>
    {% if response %}
        <p><strong>Reactie:</strong> {{ response }}</p>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        llm_output = call_llm(f"Zet deze opdracht om in JSON: '{user_input}'")
        parsed = parse_llm_response(llm_output)

        engine = SmartAssistant()
        engine.reset()
        engine.declare(Fact(location='not_home'))
        engine.declare(Fact(temperature='cold'))

        if parsed:
            engine.declare(Fact(**parsed))
            engine.run()
            response = f"Herkende intentie: {parsed.get('intent')}"
        else:
            response = "Geen geldige intentie herkend."

    return render_template_string(HTML_PAGE, response=response)


from waitress import serve

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)

```

### Resources
- [Experta Documentation](https://github.com/cordalace/experta)
- [Ollama Integration](https://ollama.ai)
- [Flask Web Framework](https://flask.palletsprojects.com/)

### Troubleshooting
| Issue | Solution |
|-------|----------|
| Assistant not responding | Ensure `Ollama` is properly installed |
| Web interface not working | Check Flask installation and API routes |
| Dependency errors | Verify packages via `pip list` |

---

*Generated using AI*