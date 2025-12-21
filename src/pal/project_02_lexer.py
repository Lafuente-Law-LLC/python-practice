
def tokenize_indentation(source: str) -> list[str]:
    tokens = []
    stack = [0]

    lines = source.splitlines()

    for line in lines:
        line_stripped = line.lstrip()
        if not line_stripped:
            continue

        indent_level = len(line) - len(line_stripped)

        if indent_level > stack[-1]:
            stack.append(indent_level)
            tokens.append("INDENT")
        elif indent_level < stack[-1]:
            while indent_level < stack[-1]:
                stack.pop()
                tokens.append("DEDENT")

            if stack[-1] != indent_level:
                raise IndentationError("warning")
    while len(stack) > 1:
        stack.pop()
        tokens.append("DEDENT")

    return tokens
