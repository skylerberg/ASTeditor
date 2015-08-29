
import sys
import ast
import _ast

globals = {}

from ASTeditor import tui
from ASTeditor.keymap import KEYMAP

def is_excluded(node):
    excluded = set([_ast.Load, _ast.Param, _ast.Store, _ast.Name, _ast.Num, _ast.alias, _ast.Call, _ast.arguments, _ast.List, _ast.ListComp, _ast.Dict, _ast.DictComp, _ast.Compare, _ast.Expr, _ast.Mod, _ast.Add])
    whitelist = set([_ast.If, _ast.FunctionDef, _ast.ClassDef, _ast.While, _ast.With, _ast.For, _ast.Module])
    for type_ in whitelist:
        if isinstance(node, type_):
            return False
    return True

def child_list(node):
    result = []
    for child in ast.iter_child_nodes(node):
        if (not is_excluded(child)):
            result.append(child)
    return result

class Node(object, ):

    def __init__(self, node, parent=None):
        self.node = node
        self.parent = parent
        self.children = []
        self.build_children()

    def build_children(self):
        self.children = []
        for child in child_list(self.node):
            self.children.append(Node(child, parent=self))

    def next_child(self, child=None):
        if (child is None):
            index = 0
        else:
            index = (self.children.index(child) + 1)
        if (index < len(self.children)):
            return self.children[index]
        return self

    def next_sibling(self):
        if (self.parent is None):
            return self.next_child()
        return self.parent.next_child(self)

    def previous_sibling(self):
        if (self.parent is None):
            return self
        self_index = self.parent.children.index(self)
        if (self_index == 0):
            return self.parent
        return self.parent.children[(self_index - 1)]

def main():
    file_name = sys.argv[1]
    with open(file_name) as file:
        tree = Node(ast.parse(file.read()))
    globals['tree'] = tree
    globals['node'] = tree
    tui.event_loop(KEYMAP)

if (__name__ == '__main__'):
    main()
