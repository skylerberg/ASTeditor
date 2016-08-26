import ast
import _ast
import unittest

from ASTeditor.editor import globals, Node
from ASTeditor import commands

SAMPLE_SOURCE = """
import sys

def main(argc, argv):
    print sys.argv[1]

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
"""


class TestNavigation(unittest.TestCase):

    def setUp(self):
        global globals
        globals["tree"] = Node(ast.parse(SAMPLE_SOURCE))
        globals["node"] = globals["tree"]

    def test_start_at_module(self):
        self.assertIsInstance(globals["node"].node, _ast.Module)

    def test_move_right(self):
        commands.next_child()
        raise Exception(ast.dump(globals["tree"].node))
        self.assertIsInstance(globals["node"].node, _ast.Import)
