# Lavai

A Python library for securely storing API keys for various AI providers locally and providing a unified client interface to interact with them.

## Features

- Secure local storage of API credentials in `~/.lavai/credentials.json`
- Unified client interface for multiple AI providers
- Command-line interface for managing credentials
- Easy-to-use Python API

## Installation

```bash
pip install lavai
```

## Usage

### Command-Line Interface

```bash
# Add or update credentials for a provider
lavai add openai "your-api-key"

# Remove credentials for a provider
lavai remove openai

# Override credentials for a provider (same as add)
lavai override openai "new-api-key"
```

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
```

## Supported Providers

- OpenAI

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

## API Reference

### `lavai.store(client_name: str, api_key: str, base_url: str = None)`

Store or update credentials for a client.

**Parameters:**
- `client_name` (str): Name of the client/provider
- `api_key` (str): API key for the client
- `base_url` (str, optional): Base URL for the client

### `lavai.client(provider_name: str)`

Get a client object for the specified provider.

**Parameters:**
- `provider_name` (str): Name of the provider (e.g., 'openai')

**Returns:**
- Client object with a unified interface

### `lavai.remove(client_name: str)`

Remove credentials for a client.

**Parameters:**
- `client_name` (str): Name of the client/provider

**Returns:**
- `True` if client was removed, `False` if client didn't exist

## CLI Commands

### `lavai add <client_name> <api_key>`

Add or update credentials for a client.

### `lavai remove <client_name>`

Remove credentials for a client.

### `lavai override <client_name> <api_key>`

Override credentials for a client (same as add).

## License

MIT
