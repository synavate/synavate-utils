import click
import yaml
from colorama import Fore, Style  # for color support

@click.command()
@click.option("--name", prompt="Project name", help="Name of the project")
@click.option("--initial_version", prompt="Initial version", help="Initial version of the project")
@click.option("--author", prompt="Author", help="Author of the project")
@click.option("--description", prompt="Description", help="Description of the project")
@click.option("--license", prompt="License", help="License of the project")
def select_library(name, initial_version, author, description, license):
    """CLI tool to select a library."""
    with open("ml-library-options.yaml", "r") as file:
        options = yaml.safe_load(file)

    active_libraries = {name: status for name, status in options["libraries"].items() if status["active"]}
    index_configs = {index: name for index, name in enumerate(active_libraries.keys(), start=1)}

    # Print project config
    click.echo(f"Project Name: {Fore.BLUE}{name}{Style.RESET_ALL}")
    click.echo(f"Initial Version: {Fore.BLUE}{initial_version}{Style.RESET_ALL}")
    click.echo(f"Author: {Fore.BLUE}{author}{Style.RESET_ALL}")
    click.echo(f"Description: {Fore.BLUE}{description}{Style.RESET_ALL}")
    click.echo(f"License: {Fore.BLUE}{license}{Style.RESET_ALL}")

    # Write project config to file
    project_config = {
        "name": name,
        "initial_version": initial_version,
        "author": author,
        "description": description,
        "license": license
    }
    lang = "python"  # Assuming the project language is Python
    with open(f"config-NAME.yaml", "w") as outfile:
        yaml.dump(project_config, outfile)

    # Print instructions
    click.echo("\nSelect a library:")

    # Display active libraries
    for index, (library, status) in enumerate(active_libraries.items(), start=1):
        click.echo(f"{Fore.BLUE}{index}. {library}{Style.RESET_ALL}")

    # Prompt user to select a library
    selection = click.prompt("Enter the number of your selection", type=int)

    # Validate user input
    if selection < 1 or selection > len(active_libraries):
        click.echo(f"{Fore.RED}Invalid selection. Please enter a number between 1 and {len(active_libraries)}{Style.RESET_ALL}")
        return

    # Get selected library
    selected_library = list(active_libraries.keys())[selection - 1]
    click.echo(f"You selected: {Fore.GREEN}{selected_library}{Style.RESET_ALL}")
    
    # Configs and indexes
    for selected_library in options["libraries"]:
        click.echo(f"Configs: {Fore.BLUE}{options['libraries'][selected_library]['configs']}{Style.RESET_ALL}")
        click.echo(f"Indexes: {Fore.BLUE}{options['libraries'][selected_library]['indexes']}{Style.RESET_ALL}")

if __name__ == "__main__":
    select_library()
