import base64
import json
import os
import sys

from argparse import Namespace
from pathlib import Path

import pytest
import requests
import wheel_inspect

import phtoolbox

from phtoolbox.deps import deps


def test_bad_command(monkeypatch):
    '''Test that nonsense command returns 2'''
    monkeypatch.setattr("sys.argv", ["phantom", "nonsense"])
    e = pytest.raises(SystemExit, phtoolbox.main)
    assert e.value.code == 2


def test_no_args(monkeypatch, capsys):
    '''Test that no command returns 1 and help message is shown. '''
    monkeypatch.setattr("sys.argv", ["phantom"])
    e = pytest.raises(SystemExit, phtoolbox.main)
    assert e.value.code == 1

    captured = capsys.readouterr()
    assert "usage" in captured.err
    assert captured.out == ""


class postResult():
    def json(self):
        return self._json

    def __init__(self, status_code, text, json):
        self.status_code = status_code
        self.text = text
        self._json = json


@pytest.mark.parametrize(
    "json_data,return_code",
    [
        ("", 0),        # Happy path
        ("failed", 1),  # Server returns error
    ],
)
def test_deploy(monkeypatch, tmp_path, json_data, return_code):
    '''Test that help message is shown when no args given.'''
    file = tmp_path / "foo"
    file.write_text("bar")

    monkeypatch.setenv("SOAR_TOKEN", "FAKE_TOKEN")
    monkeypatch.setenv("SOAR_HOSTNAME", "127.0.0.1")

    def mock_post(url, headers, data):
        assert url == "https://127.0.0.1/rest/app"
        assert headers == {'ph-auth-token': "FAKE_TOKEN"}
        assert json.loads(data) == {
            'app': base64.b64encode(b'bar').decode('ascii')
        }
        return postResult(requests.codes.ok, "", json_data)
    monkeypatch.setattr(requests, "post", mock_post)

    monkeypatch.setattr(
        "sys.argv",
        ["phantom", "deploy", str(file.absolute())]
    )
    e = pytest.raises(SystemExit, phtoolbox.main)
    assert e.value.code == return_code


@pytest.mark.parametrize(
    "input_json",
    [
        {"some_key": "some_value"},
        {"some_key": "some_value", "pip3_dependencies": {}},
        {"some_key": "some_value", "pip3_dependencies": {"wheel": []}},
    ],
)
def test_deps(monkeypatch, capsys, input_json):
    '''Test deps command'''
    args = Namespace()
    args.dir = ["wheels"]
    args.input_file = input_json
    args.output_file = sys.stdout

    def mock_listdir(path):
        assert path == "wheels"
        return ["example.whl"]

    def mock_inspect_wheel(fpath):
        assert fpath == Path("wheels") / "example.whl"
        return {
            'dist_info': {'metadata': {'name': 'example_module'}}
        }

    monkeypatch.setattr(os, "listdir", mock_listdir)
    monkeypatch.setattr(wheel_inspect, "inspect_wheel", mock_inspect_wheel)

    deps(args)

    captured = capsys.readouterr()
    output = json.loads(captured.out)

    assert output == {
        "some_key": "some_value",
        "pip3_dependencies": {
            "wheel": [
                {
                    "module": "example_module",
                    "input_file": "wheels/example.whl"
                }
            ]
        }
    }
