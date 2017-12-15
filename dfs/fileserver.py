import logging
import os.path
import time

from contextlib import closing
from http.client import HTTPConnection

import web

import utils

class FileServer:
    #Fileserver for holding & sharing

    def GET(self, filepath):
        #Return the requested file if it's not locked

        web.header('Content-Type', 'text/plain; charset=UTF-8')
        return ''

    def PUT(self, filepath):
        #Replace the file by the data in the request.

        return ''

    def DELETE(self, filepath):
        #Remove the filepath if it's unlocked
        return ''

    def HEAD(self, filepath):
        #If the file exists/isn't locked, return the last-modified http header

        return ''

def _get_local_path(filepath):
    #Convert the filepath uri in the FS.

    return os.path.join(os.getcwd(), _config['fsroot'], filepath[1:])


def _raise_if_locked(filepath):
    #Raise a 401 unauthorized locked filepath
    pass


def _raise_if_dir_or_not_servable(filepath):
    #Raise 406 if not servable
    pass


def _raise_if_not_exists(filepath):
    pass

def _init_file_server():
    #notify the nameserver about out directories
    pass


_config = {
        'lockserver': None,
        'nameserver': None,
        'directories': [],
        'fsroot': 'fs/',
        'srv': None,
        }

logging.info('Loading config file fileserver.dfs.json.')
_config['directories'] = set(_config['directories'])

_init_file_server()
