from ASTeditor import commands

KEYMAP = {
    'f': commands.build_function,
    'p': commands.build_pass,
    'b': commands.build_break,
    'c': commands.build_continue,
    'h': commands.parent_node,
    'j': commands.next_sibling,
    'k': commands.previous_sibling,
    'l': commands.next_child,
    's': commands.save,
    'd': commands.delete_node,
    'm': commands.build_import,
    'i': commands.build_if,
    'e': commands.build_expr,
    '4': commands.build_for,
    'q': exit,
}
