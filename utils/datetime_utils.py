from datetime import datetime

def format_timestamp(timestamp):
    """
    Converts a timestamp (integer) to a formatted date string.

    Args:
        timestamp (int): The Unix timestamp.

    Returns:
        str: Formatted date string in "YYYY-MM-DD" format.
    """
    if isinstance(timestamp, int):
        try:
            date_obj = datetime.fromtimestamp(timestamp)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            return f"Error: {e}"
    else:
        return "Invalid input: Timestamp must be an integer."