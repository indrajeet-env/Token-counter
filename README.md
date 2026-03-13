# Token Counter

A simple Python utility to count tokens used in LLM prompts and responses.

## Setup

1. Create a virtual environment (recommended)

```bash
python3 -m venv .venv
```

2. Activate the virtual environment

Mac / Linux:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python token_counter.py
```

You will be asked to enter:

- Task name
- Prompt text
- Response text

The script will display:

- Prompt tokens
- Response tokens
- Total tokens

Token usage is also logged in `token_usage_log.md`.
