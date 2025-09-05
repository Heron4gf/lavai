import json
import os
from pathlib import Path
from typing import Optional


def get_credentials_path() -> Path:
    """Get the path to the credentials file."""
    home = Path.home()
    lavai_dir = home / '.lavai'
    return lavai_dir / 'credentials.json'


def ensure_credentials_file() -> Path:
    """Ensure the credentials file exists and return its path."""
    credentials_path = get_credentials_path()
    
    # Create directory if it doesn't exist
    credentials_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create file if it doesn't exist
    if not credentials_path.exists():
        credentials_path.write_text('{}')
    
    return credentials_path


def load_credentials() -> dict:
    """Load credentials from the JSON file."""
    credentials_path = ensure_credentials_file()
    
    try:
        with open(credentials_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If file is corrupted, return empty dict and recreate file
        with open(credentials_path, 'w') as f:
            json.dump({}, f)
        return {}


def save_credentials(credentials: dict) -> None:
    """Save credentials to the JSON file."""
    credentials_path = ensure_credentials_file()
    
    with open(credentials_path, 'w') as f:
        json.dump(credentials, f, indent=2)


def store(client_name: str, api_key: str, base_url: Optional[str] = None) -> None:
    """
    Store or update credentials for a client.
    
    Args:
        client_name: Name of the client/provider
        api_key: API key for the client
        base_url: Optional base URL for the client
    """
    credentials = load_credentials()
    
    client_data = {'api_key': api_key}
    if base_url is not None:
        client_data['base_url'] = base_url
    
    credentials[client_name] = client_data
    save_credentials(credentials)


def remove(client_name: str) -> bool:
    """
    Remove credentials for a client.
    
    Args:
        client_name: Name of the client/provider
        
    Returns:
        True if client was removed, False if client didn't exist
    """
    credentials = load_credentials()
    
    if client_name in credentials:
        del credentials[client_name]
        save_credentials(credentials)
        return True
    return False
