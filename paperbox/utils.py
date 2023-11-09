import yaml
from typing import Dict


def get_config() -> Dict:
    """Get the PaperBox config."""
    with open("paperbox_config.yml", "r") as f:
        return yaml.safe_load(f)
