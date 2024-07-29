import pytest

from brackets import check_correct_brackets


class TestBrackets:

    @pytest.mark.parametrize(
        "input_string, expected",
        [
            ("(((([{}]))))", True),
            ("[([])((([[[]]])))]{()}", True),
            ("{{[()]}}", True),
        ]
    )
    def test_correct_brackets(self, input_string, expected):
        assert check_correct_brackets(input_string) == expected

    @pytest.mark.parametrize(
        "input_string, expected",
        [
            ("}{}", False),
            ("{{[(])]}}", False),
            ("[[{())}]", False),
        ]
    )
    def test_not_correct_brackets(self, input_string, expected):
        assert check_correct_brackets(input_string) == expected
