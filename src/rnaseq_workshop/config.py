"""Load and check a group's analysis configuration."""

from pathlib import Path

import yaml

REQUIRED_SECTIONS = ("group", "dataset", "paths", "design", "thresholds")


def load_config(path: str | Path) -> dict:
    """Read a group's ``config.yaml`` and check that the main sections are present.

    Parameters
    ----------
    path : str or Path
        Path to the YAML configuration file.

    Returns
    -------
    dict
        The parsed configuration.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    ValueError
        If a required section is missing.
    """
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open() as handle:
        config = yaml.safe_load(handle) or {}

    missing = [section for section in REQUIRED_SECTIONS if section not in config]
    if missing:
        raise ValueError(f"{path} is missing required section(s): {', '.join(missing)}")

    return config
