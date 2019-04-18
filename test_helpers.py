import pytest

from backend_epithet_generator.app import app
# importing from inside app need the fodler.w;/e

from backend_epithet_generator.helpers import Vocabulary as V
# from .helpers import EpithetGenerator as EpG

data = V.read_json("resources/data.json")


def test_read_json_success():
    # test output odf rjl check that func did well
    assert isinstance(data, dict)
    # num keys; check specific words in data cols; test about data is coming in
    # assert data != "resources/data.json"


# def test_read_json_fail():
#     V().read_json()
#     assert
    # what will happen if we ask it to do the wrong way
    # pass python file; bad path; dict or string
    # fail how we expect it


# def test_generate_one_success():
#     EpG().generate_one()
#     assert


# def test_generate_one_fail():
#     EpG().generate_one()
#     assert


# def test_generate_multi_success():
#     EpG().generate_multi()
#     assert


# def test_generate_multi_fail():
#     EpG().generate_multi()
#     assert
