import json

def load_data(filename):
    """
    Load JSON data from a file.
    Returns an empty dict if file doesn't exist or is invalid.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(filename, data):
    """
    Save datato json with indentation for readability
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
