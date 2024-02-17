from datetime import datetime

def get_current_timestamp():
    """Get the current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_elapsed_time(start_time, end_time):
    """Calculate elapsed time."""
    return end_time - start_time

