import json

from .calc.calc import CalcConnector

APP_ID = "tacosalad"


def test_nice_connector_add(connector: CalcConnector):
    in_json = {
            "appid": APP_ID,
            "identifier": "add",
            "parameters": [{
                "x": 2,
                "y": 1,
            }],
    }

    result = json.loads(connector._handle_action(json.dumps(in_json), None))
    assert result[0]["message"] == "Sum 3"


def test_nice_connector_subtract(connector: CalcConnector):
    in_json = {
            "appid": APP_ID,
            "identifier": "subtract",
            "parameters": [{
                "x": 2,
                "y": 1,
            }],
    }

    result = json.loads(connector._handle_action(json.dumps(in_json), None))
    assert result[0]["message"] == "Difference 1"
