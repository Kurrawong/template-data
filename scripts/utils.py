import os
from pathlib import Path


def ensure_data_dir_exists(dir: Path):
    """Create `data/` directory if doesn't exist"""
    os.makedirs(dir / "data", exist_ok=True)
