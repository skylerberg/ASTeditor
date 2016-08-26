import curses
from astunparse import unparse
from ASTeditor.editor import globals

SCREEN = None
KEYMAP = None

def menu(*args):
    curses.echo()
    screen = SCREEN
    screen.erase()
    results = {}
    for arg in args:
        screen.addstr(('%s: ' % arg))
        screen.refresh()
        value = screen.getstr()
        results[arg] = value
    curses.noecho()
    return results

def _display():
    screen = SCREEN
    node = globals['node']
    screen.erase()
    (y, x) = screen.getmaxyx()
    for (num, line) in enumerate(unparse(node.node).split('\n')):
        if (num >= y):
            break
        screen.addnstr(num, 0, line, (x - 1))
    screen.refresh()

def event_loop(keymap):
    global KEYMAP
    KEYMAP = keymap
    curses.wrapper(_event_loop)

def _event_loop(screen):
    global SCREEN
    SCREEN = screen
    curses.noecho()
    while True:
        _display()
        key = screen.getkey()
        if key in KEYMAP:
            KEYMAP[key]()
