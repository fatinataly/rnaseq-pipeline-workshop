from pathlib import Path

import pytest

from rnaseq_workshop import load_config

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("group", ["group-a", "group-b"])
def test_group_configs_load(group):
    config = load_config(REPO_ROOT / "groups" / group / "config" / "config.yaml")
    assert config["group"] == group


def test_missing_section_raises(tmp_path):
    bad = tmp_path / "config.yaml"
    bad.write_text("group: group-a\n")
    with pytest.raises(ValueError, match="missing required section"):
        load_config(bad)


def test_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_config(tmp_path / "does_not_exist.yaml")
