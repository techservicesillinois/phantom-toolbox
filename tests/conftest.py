import logging

import pytest

from .calc.calc import CalcConnector

# Required pytest plugins
pytest_plugins = ("splunk-soar-connectors")


@pytest.fixture
def connector() -> CalcConnector:
    conn = CalcConnector()

    conn.config = {
        "x": 2,
        "y": 1,
    }

    conn.logger.setLevel(logging.INFO)
    return conn
