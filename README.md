*This project has been created as part of the 42 curriculum by mobenhab.*

# call me maybe — Introduction to Function Calling in LLMs

---

## Description

**call me maybe** is a function-calling engine that bridges natural language and structured computation. Given a plain-English prompt such as *"What is the sum of 40 and 2?"*, the program does **not** answer `42` — instead, it produces a structured function call:

```json
{
  "function": "fn_add_numbers",
  "arguments": { "a": 40, "b": 2 }
}
```

The system reads a set of available function definitions and a list of natural language prompts, then uses a small 0.5B-parameter LLM to map each prompt to the correct function and arguments. The key constraint is reliability: by applying **constrained decoding**, the output is guaranteed to be 100% valid JSON that conforms to the expected schema — even with a tiny model that would otherwise hallucinate or produce malformed output.

This project is an introduction to how modern AI assistants (ChatGPT, Claude, Gemini…) implement tool/function calling under the hood.

---



## Instructions

### Requirements

- Python 3.10+
- The `llm_sdk` package (provided with the project)
- Dependencies listed in `requirements.txt`

### Installation

```bash
git clone <your-repo-url>
cd call-me-maybe
pip install -r requirements.txt
```