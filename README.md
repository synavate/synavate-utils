# Synavate Utilities Package

# Project Name

Synavate project utilities

## Overview

Brief overview of what the project does and its purpose.

## Installation

```bash
# Clone the repository
git clone https://github.com/synavate/synavate-utils.git
cd synavate-utils

# Install dependencies
poetry install
```

## Usage

```bash
# Run the project
python main.py
```

## Configuration

The project uses a configuration file located at `config/config.json`. Modify this file to adjust project settings.

## Contributing

To contribute to the project, follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/new-feature`)
6. Create a new Pull Request

## License

Information about the project's license.

## GitHub Action for Build

We have included a GitHub Action for automatic builds. The action is triggered whenever changes are pushed to the repository. It will build the project and create distribution packages (e.g., wheels or source distributions) in the `dist` directory.

To use the GitHub Action, simply push your changes to the repository, and the build process will be automatically triggered. You can find more information about GitHub Actions in the [official documentation](https://docs.github.com/en/actions).

