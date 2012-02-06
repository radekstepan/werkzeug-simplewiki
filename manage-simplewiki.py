#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Manage SimpleWiki
    ~~~~~~~~~~~~~~~~~

    This script provides some basic commands to debug and test SimpleWiki.

    :copyright: (c) 2009 by the Werkzeug Team, see AUTHORS for more details.
    :license: BSD, see LICENSE for more details.
"""
import os, sys
from werkzeug import script

SIMPLEWIKI_DATABASE_URI = 'db/sqlite.db'

def make_wiki():
    """Helper function that creates a new wiki instance."""
    from app import SimpleWiki
    return SimpleWiki('sqlite:///%s/%s' % (sys.path[0], SIMPLEWIKI_DATABASE_URI))


def shell_init_func():
    """
    Called on shell initialization.  Adds useful stuff to the namespace.
    """
    from app import database
    wiki = make_wiki()
    wiki.bind_to_context()
    return {
        'wiki':     wiki,
        'db':       database
    }


action_runserver = script.make_runserver(make_wiki, use_reloader=True)
action_shell = script.make_shell(shell_init_func)


def action_initdb():
    """Initialize the database"""
    make_wiki().init_database()

if __name__ == '__main__':
    script.run()