from typing import Optional
import openai
from .credentials import load_credentials
from .responses import Responses


class WrappedClient:
    """Wrapped client with standardized interface."""
    
    def __init__(self, client):
        self._client = client
        self.responses = Responses(client)


def client(provider_name: str):
    """
    Get a client object for the specified provider.
    
    Args:
        provider_name: Name of the provider (e.g., 'openai')
        
    Returns:
        Wrapped client object with standardized interface
        
    Raises:
        ValueError: If provider is not supported or credentials are missing
    """
    credentials = load_credentials()
    
    if provider_name not in credentials:
        raise ValueError(f"No credentials found for provider '{provider_name}'")
    
    provider_credentials = credentials[provider_name]
    
    if provider_name == 'openai':
        openai_client = openai.OpenAI(
            api_key=provider_credentials['api_key'],
            base_url=provider_credentials.get('base_url')
        )
        return WrappedClient(openai_client)
    else:
        raise ValueError(f"Provider '{provider_name}' is not supported")
