import os
import yaml

def load_config():
    """Loads the cofig file"""
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)