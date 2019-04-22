from backend_epithet_generator.app import app

import json


def test_app_gen_one():
    with app.test_client() as cli:
        result = cli.get("/")
        assert result.status_code == 200
        data = result.data.decode()
        assert isinstance(data, str)
        jsonified_data = json.loads(data)
        assert "!" in jsonified_data["epithets"]


def test_app_vocab():
    result = app.test_client().get("/vocabulary")
    assert result.status_code == 200
    assert result.data.decode()


def test_app_gen_multi():
    result = app.test_client().get("/epithets/<int:quantity>")
    assert result.data.decode()


def test_app_randomizeme():
    result = app.test_client().get("/randomizeme")
    assert result.status_code == 200
    assert result.data.decode()
