import pytest

from backend_epithet_generator.app import app
# importing from inside app need the fodler.w/e

from backend_epithet_generator.helpers import Vocabulary as V
from .helpers import EpithetGenerator as EpG

json_data = V.read_json("resources/data.json")
single_epi = EpG().generate_one()
multi_epi = EpG().generate_multi(3)  # testing for 3 epithets


def test_read_json_success():
    # test output of r_j; check that func did well
    assert isinstance(json_data, dict)
    # num keys in dict; check specific words in data cols; test data coming in
    assert len(json_data.keys()) == 3
    assert "qualling" in json_data["Column 1"]
    assert "whoreson" in json_data["Column 2"]
    assert "fustilarian" in json_data["Column 3"]
    assert "Column 666" not in json_data.keys()


def test_read_json_fail():
    # what will happen if we ask it to do the wrong way?
    # pass python file; bad path; dict or string
    # fail how we expect it

    # check what should be riased!!!!!!!!!
    # AE for when an assert fails
    with pytest.raises(AssertionError):
        assert isinstance(json_data, str)
    with pytest.raises(AssertionError):
        assert len(json_data.keys()) == "Not a key"
    # assert "Not in Column 1" not in json_data["Column 1"]
    with pytest.raises(AssertionError):
        assert "Not in Column 1" in json_data["Column 1"]
    with pytest.raises(AssertionError):
        assert "Not in Column 2" in json_data["Column 2"]
    with pytest.raises(AssertionError):
        assert "Not in Column 3" in json_data["Column 3"]
    with pytest.raises(KeyError):
        assert json_data["Column 666"]


def test_generate_one_success():
    assert isinstance(single_epi, str)
    assert len(single_epi.split(" ")) == 3
    assert single_epi.split(" ")[0] in json_data["Column 1"]
    assert single_epi.split(" ")[1] in json_data["Column 2"]


def test_generate_one_fail():
    with pytest.raises(AssertionError):
        assert isinstance(single_epi, dict)
    with pytest.raises(AssertionError):
        assert len(single_epi.split(" ")) == 333
    with pytest.raises(AssertionError):
        assert single_epi.split(" ")[2] in json_data["Column 1"]


def test_generate_multi_success():
    assert isinstance(multi_epi, list)
    assert len(multi_epi) == 3
    assert multi_epi[1].split(" ")[2].replace("!", "") in json_data["Column 3"]
    # ^^^ looking at 2nd ep's last word


def test_generate_multi_fail():
    with pytest.raises(AssertionError):
        assert isinstance(multi_epi, str)
    with pytest.raises(AssertionError):
        assert len(multi_epi) == 333
    with pytest.raises(IndexError):
        assert multi_epi[1].split(" ")[555]