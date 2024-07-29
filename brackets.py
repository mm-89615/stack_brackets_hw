from stack import Stack


def check_correct_brackets(str_: str) -> bool:
    brackets = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for bracket in str_:
        if bracket not in brackets:
            stack.push(bracket)
        else:
            if stack.is_empty():
                return False
            last_bracket = stack.pop()
            if last_bracket != brackets[bracket]:
                return False
    return True
