# pylint: disable=redefined-outer-name
# pylint: disable=missing-function-docstring
import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    utils = StringUtils()
    return utils


def test_fixture_creates_new_instance(string_utils):
    assert isinstance(string_utils, StringUtils)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
    ],
)
def test_capitalize_positive(string_utils, input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("SKYPRO", "Skypro"),
        ("123abc", "123abc"),
        ("!hello", "!hello"),
        ("", ""),
        ("   ", "   "),
    ],
)
def test_capitalize_negative(string_utils, input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("  skypro", "skypro"),
        ("hello world", "hello world"),
        ("  python  ", "python  "),
    ],
)
def test_trim_positive(string_utils, input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [("   ", ""), ("", "")],
)
def test_trim_negative(string_utils, input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str,input_symbol, expected",
    [("SkyPro", "k", True), ("SkyPro", "Z", False)],
)
def test_contains_positive(string_utils, input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str,input_symbol, expected",
    [("", "", True), ("SkyPro", "Pro", True)],
)
def test_contains_negative(string_utils, input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


def test_contains_invalid_types(string_utils):
    with pytest.raises(TypeError):
        string_utils.contains(123, 1)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str,input_symbol, expected",
    [("SkyPro", "k", "SyPro"), ("SkyPro", "Pro", "Sky"), ("aaa", "a", (""))],
)
def test_delete_symbol_positive(string_utils, input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str,input_symbol, expected",
    [("SkyPro", "l", "SkyPro"), ("", "P", ""), ("SkyPro", "", "SkyPro")],
)
def test_delete_symbol_negative(string_utils, input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected
