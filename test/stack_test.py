import pytest

from stack import Stack


class TestStack:
    def setup_class(self):
        self.stack = Stack()

    def test_is_empty(self):
        assert self.stack.is_empty()

    @pytest.mark.parametrize(
        "value, expected",
        [
            (1, 1),
            ('str_test', 2),
            ([1, 2, 3], 3),
            ({1: 1}, 4),
            ({'a', 'b'}, 5),
        ]
    )
    def test_push(self, value, expected):
        self.stack.push(value)
        assert self.stack.size() == expected

    @pytest.mark.parametrize(
        "expected, len_stack",
        [
            ({'a', 'b'}, 4),
            ({1: 1}, 3),
        ]
    )
    def test_pop(self, expected, len_stack):
        value = self.stack.pop()
        assert value == expected
        assert self.stack.size() == len_stack

    def test_peek(self):
        len_before = self.stack.size()
        value = self.stack.peek()
        assert value == [1, 2, 3]
        assert self.stack.size() == len_before

    @pytest.mark.parametrize(
        "push_value, size_stack",
        [
            (1, 4),
            (2, 5),
        ]
    )
    def test_size(self, push_value, size_stack):
        self.stack.push(push_value)
        assert self.stack.size() == size_stack
