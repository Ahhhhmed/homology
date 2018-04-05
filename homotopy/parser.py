from homotopy.syntax_tree import SimpleSnippet, CompositeSnippet


class Parser:
    parameter_chars = "!@#$%:~"
    in_operator = '>'
    out_operator = '<'
    and_operator = '&'

    @staticmethod
    def parse(snippet_text):
        stack = []
        current_match = []
        last_operator = Parser.in_operator

        for c in snippet_text + "\0":
            if c in Parser.parameter_chars or c in ["\0", Parser.in_operator, Parser.out_operator, Parser.and_operator]:
                if last_operator == Parser.in_operator:
                    stack.append(SimpleSnippet("".join(current_match)))
                else:
                    current_snippet = stack.pop()
                    stack.append(
                        CompositeSnippet(current_snippet, last_operator, SimpleSnippet("".join(current_match))))

                last_operator = c
                current_match.clear()
            else:
                current_match.append(c)

            if c == Parser.and_operator:
                last_operator = Parser.in_operator
                Parser.merge_stack(stack)

            if c == Parser.out_operator:
                last_operator = Parser.in_operator

                for _ in range(2):
                    Parser.merge_stack(stack)

        while len(stack) > 1:
            Parser.merge_stack(stack)

        return stack.pop()

    @staticmethod
    def merge_stack(stack):
        last_tree = stack.pop()
        if last_tree != SimpleSnippet(''):
            next_tree = stack.pop()
            stack.append(CompositeSnippet(next_tree, Parser.in_operator, last_tree))


parser = Parser()
