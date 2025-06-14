import yaml
from pathlib import Path

def load_config(config_path: str = "config.yaml") -> dict:
    """Load and parse the YAML configuration file."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
