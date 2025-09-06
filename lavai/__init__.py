"""
Lavai - A Python library for securely storing API keys for various AI providers locally 
and providing a unified client interface to interact with them.

Features:
- Secure local storage of API credentials in ~/.lavai/credentials.json
- Unified client interface for multiple AI providers
- Command-line interface for managing credentials
- Easy-to-use Python API

Example usage:
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
"""

from .credentials import store, remove, list_clients
from .client import client

__all__ = ['store', 'client', 'remove', 'list_clients']
__version__ = '0.1.0'
