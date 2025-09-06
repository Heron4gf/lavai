import click
from .credentials import store, remove as remove_credentials, list_clients


@click.group()
def main():
    """Lavai CLI for managing AI provider credentials."""
    pass


@main.command()
@click.argument('client_name')
@click.argument('api_key')
def add(client_name, api_key):
    """Add or update credentials for a client."""
    store(client_name, api_key)
    click.echo(f"Credentials for '{client_name}' have been stored.")


@main.command()
@click.argument('client_name')
def remove(client_name):
    """Remove credentials for a client."""
    if remove_credentials(client_name):
        click.echo(f"Credentials for '{client_name}' have been removed.")
    else:
        click.echo(f"No credentials found for '{client_name}'.")


@main.command()
@click.argument('client_name')
@click.argument('api_key')
def override(client_name, api_key):
    """Override credentials for a client (same as add)."""
    store(client_name, api_key)
    click.echo(f"Credentials for '{client_name}' have been updated.")


@main.command()
def list():
    """List all configured clients."""
    clients = list_clients()
    if clients:
        click.echo("Configured clients:")
        for client in clients:
            click.echo(f"  - {client}")
    else:
        click.echo("No clients configured.")


if __name__ == '__main__':
    main()
