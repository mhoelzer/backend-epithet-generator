from backend_epithet_generator.app import app
from backend_epithet_generator.helpers import Vocabulary as V
import json

json_data = V.read_json("resources/data.json")


def test_app_gen_one():
    with app.test_client() as cli:
        response = cli.get("/")
        data = response.data.decode()
        assert isinstance(data, str)
        result = json.loads(data)
        assert response.status_code == 200
        assert "epithets" in result

# def test_app_vocab():
#     result = app.test_client().get("/vocabulary")
#     assert result.data.decode() == json_data
