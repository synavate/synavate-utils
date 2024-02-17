import os
import sys
import logging

def setup_logging(log_file="app.log", level=logging.INFO):
    """Set up logging configuration."""
    logging.basicConfig(
        filename=log_file,
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=level
    )

def get_logger(name=__name__):
    """Get a logger instance."""
    return logging.getLogger(name)

def create_directory(directory):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def delete_file(file_path):
    """Delete a file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)

def list_files(directory):
    """List files in a directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def check_python_version(major=3, minor=6):
    """Check if the Python version meets the required minimum."""
    if sys.version_info < (major, minor):
        print(f"Python {major}.{minor} or later is required.")
        sys.exit(1)

def get_system_info():
    """Get system information."""
    return {
        "python_version": sys.version,
        "platform": sys.platform,
        "architecture": platform.architecture()
        # Add more system info as needed
    }
