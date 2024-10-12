from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def assets() -> Path:
    return Path(__file__).parent / "assets"
