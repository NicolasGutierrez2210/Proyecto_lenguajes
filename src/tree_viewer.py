from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl
from antlr4 import ParserRuleContext


def format_parse_tree(node, parser, prefix="", is_last=True) -> str:
    lines = []
    marker = "\\-- " if is_last else "|-- "

    if isinstance(node, (TerminalNodeImpl, ErrorNodeImpl)):
        token = node.getSymbol()
        text = token.text
        if text == "<EOF>":
            node_label = "<EOF>"
        else:
            token_name = parser.symbolicNames[token.type] if token.type < len(parser.symbolicNames) else "TOKEN"
            node_label = f"'{text}' ({token_name})"
    elif isinstance(node, ParserRuleContext):
        rule_name = parser.ruleNames[node.getRuleIndex()]
        node_label = f"<{rule_name}>"
    else:
        node_label = str(type(node).__name__)

    lines.append(f"{prefix}{marker}{node_label}")

    child_prefix = prefix + ("    " if is_last else "|   ")
    child_count = node.getChildCount() if hasattr(node, "getChildCount") else 0

    for i in range(child_count):
        child = node.getChild(i)
        is_child_last = (i == child_count - 1)
        lines.append(format_parse_tree(child, parser, child_prefix, is_child_last))

    return "\n".join(lines)


def print_parse_tree(tree, parser) -> None:
    print(format_parse_tree(tree, parser))
