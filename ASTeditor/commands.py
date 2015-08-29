import sys
import _ast
import ast
from astunparse import unparse
from ASTeditor.editor import globals
from ASTeditor.tui import menu

def next_child():
    node = globals["node"]
    globals["node"] = node.next_child()

def next_sibling():
    node = globals["node"]
    globals["node"] = node.next_sibling()

def previous_sibling():
    node = globals["node"]
    globals["node"] = node.previous_sibling()

def parent_node():
    globals["node"] = globals["node"].parent or globals["node"]

def add_ast_node(node):
    parent = globals['node']
    parent.node.body.append(node)
    parent.build_children()

def build_function():
    config = menu('name')
    name = config['name']
    function = _ast.FunctionDef(name=name, args=[], defaults=[], body=[], decorator_list=[])
    add_ast_node(function)
    parent = globals['node']
    for child in parent.children:
        if (child.node == function):
            globals['node'] = child
            break

def build_pass():
    add_ast_node(_ast.Pass())

def build_continue():
    add_ast_node(_ast.Continue())

def build_break():
    add_ast_node(_ast.Break())

def delete_node():
    current = globals["node"]
    parent = current.parent
    if parent is None:
        return
    for field in parent.node._fields:
        filtered = [node for node in getattr(parent.node, field) if node != current.node]
        setattr(parent.node, field, filtered)
    parent.build_children()
    globals["node"] = parent



def save():
    file_name = sys.argv[1]
    output = unparse(globals['tree'].node)
    with open(file_name, 'w') as file:
        file.write(output)
