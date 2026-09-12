"""
AIKReporter - Config Manager
Save and load API credentials from a JSON file
"""

import os
import json


CONFIG_FILE = "config.json"


def save_config(api_id, api_hash, phone):
    """Save API credentials to file"""
    data = {
        "api_id": api_id,
        "api_hash": api_hash,
        "phone": phone
    }
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"[+] Config saved to {CONFIG_FILE}")


def load_config():
    """Load API credentials from file"""
    if not os.path.exists(CONFIG_FILE):
        return None

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Check all required keys exist
        if all(k in data for k in ("api_id", "api_hash", "phone")):
            return data
        return None
    except (json.JSONDecodeError, KeyError):
        return None


def delete_config():
    """Delete config file"""
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)
        print(f"[-] Config deleted")