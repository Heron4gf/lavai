# Lavai

[![MIT License](https://img.shields.io/badge/MIT-green?style=for-the-badge)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)](https://github.com/Heron4gf/lavai/actions)
[![PyPI Version](https://img.shields.io/pypi/v/lavai?style=for-the-badge)](https://pypi.org/project/lavai/)

A Python library for securely storing API keys for various AI providers locally and providing a unified client interface to interact with them.

## Features

- Secure local storage of API credentials in `~/.lavai/credentials.json`
- Unified client interface for multiple AI providers
- Command-line interface for managing credentials
- Easy-to-use Python API

## Installation

```bash
git clone https://github.com/Heron4gf/lavai
pip install -e .
```

## Usage

### Command-Line Interface

Manage your AI provider credentials directly from the command line:

| Command | Description | Example |
|---------|-------------|---------|
| `lavai add <client_name> <api_key>` | Add or update credentials for a provider | `lavai add openai "your-api-key"` |
| `lavai remove <client_name>` | Remove credentials for a provider | `lavai remove openai` |
| `lavai override <client_name> <api_key>` | Override credentials for a provider (same as add) | `lavai override openai "new-api-key"` |
| `lavai list` | List all configured providers | `lavai list` |

### Python API

```python
import lavai

# Store credentials
lavai.store("openai", "your-api-key")

# Create a client
client = lavai.client("openai")

# Use the unified interface to generate responses
response = client.responses.create(
    model="gpt-4",
    input="Write a short bedtime story about a unicorn."
)
print(response.output_text)

# Or use the provider's native interface
chat_completion = client._client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)

# List all configured clients
clients = lavai.list_clients()
print("Configured clients:", clients)
```

## Supported Providers

- OpenAI
- Any OpenAI client compatible provider (e.g., Anthropic, Cohere, OpenRouter, etc.)

## Credential Storage

Credentials are stored in `~/.lavai/credentials.json` with the following structure:

```json
{
  "provider_name_1": {
    "api_key": "...",
    "base_url": "..."
  },
  "provider_name_2": {
    "api_key": "...",
    "base_url": "..."
  }
}
```

The `~/.lavai/` directory and `credentials.json` file are created automatically on first use.

**!!! Security Notice !!!** secrets are stored in a plain json file, it is recommended to double check that the programs you install using lavai as dependency do not steal those keys

## API Reference

| Function | Description | Parameters |
|----------|-------------|------------|
| `lavai.store(client_name: str, api_key: str, base_url: str = None)` | Store or update credentials for a client | `client_name`, `api_key`, `base_url` (optional) |
| `lavai.client(provider_name: str)` | Get a client object for the specified provider | `provider_name` |
| `lavai.remove(client_name: str)` | Remove credentials for a client | `client_name` |
| `lavai.list_clients()` | List all client names | None |
