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
        _raise_if_dir_or_not_servable(filepath)
        _raise_if_not_exists(filepath)
        _raise_if_locked(filepath)

        p = _get_local_path(filepath)
        web.header('Last-Modified', time.ctime(os.path.getmtime(p)))
        with open(p) as f:
            return f.read()
        

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
    p = _get_local_path(filepath)

    if (os.path.dirname(filepath) not in _config['directories'] or
            os.path.isdir(p)):
        # request a file which this server isn't supposed to serve!
        raise web.notacceptable()


def _raise_if_not_exists(filepath):
    p = _get_local_path(filepath)

    if not os.path.exists(p):
        raise web.webapi.HTTPError('204 No Content', {'Content-Type': 'plain/text'})
    

def _init_file_server():
    host, port = utils.get_host_port(_config['nameserver'])
    with closing(HTTPConnection(host, port)) as con:
        data = 'srv=%s&dirs=%s' % (_config['srv'], '\n'.join(_config['directories']),)
        con.request('POST', '/', data)
    

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
