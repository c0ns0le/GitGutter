# -*- coding: utf-8 -*-
import sublime

PLATFORM = sublime.platform()
WIN32 = PLATFORM == 'windows'

STVER = int(sublime.version())
ST3 = STVER >= 3000


def log_message(msg):
    """Print a message to statusbar and log in console."""
    msg = 'GitGutter: {0}'.format(msg)
    print(msg)
    sublime.status_message(msg)
