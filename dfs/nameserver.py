import atexit
import logging
import os
import shelve

import web

import utils

class NameServer:
    #NameServer is responsible of the mapping between directory names and file servers.

    def GET(self, filepath):
        #Return a server which hold the directory in which filepath is located

        web.header('Content-Type', 'text/plain; charset=UTF-8')
        filepath = str(filepath)

        return''

    def POST(self, dirpath):
        """See _update (with add=True)."""

        return _update(str(dirpath))

    def DELETE(self, dirpath):
        """See _update (with add=False)."""

        return _update(str(dirpath), False)


def _update(dirpath, add=True):
    #Add pair of directory/server to the name server if ADD= TRUE else REMOVE(DELETE)

    web.header('Content-Type', 'text/plain; charset=UTF-8')
    return ''


def _update_names(dirpath, srv, add=True):
    #Just update the name dictionary and the database.
    return ''


_config = {
            'dbfile': 'names.db',
         }

logging.info('Loading config file nameserver.dfs.json.')
utils.load_config(_config, 'nameserver.dfs.json')
_names = shelve.open(_config['dbfile'])

atexit.register(lambda: _names.close())
