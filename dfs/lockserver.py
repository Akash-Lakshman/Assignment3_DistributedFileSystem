import atexit
import collections
import copy
import datetime
import logging
import os.path
import random
import shelve

import web


Lock = collections.namedtuple('Lock', 'lock_id granted last_used')

class LockServer:
    #Server Responsible of handling locking on files

    def GET(self, filepath):

        web.header('Content-Type', 'text/plain; charset=UTF-8')
        filepath = str(filepath)
        i = web.input()

        if filepath == '/':
            return ''
        elif _lock_expired(filepath):
            _revoke_lock(filepath)
            return 'OK'

        #Raise conflict in case already locked
        raise web.conflict()


    def POST(self, filepath):

        web.header('Content-Type', 'text/plain; charset=UTF-8')
        filepath = str(filepath)

        if filepath == '/':
            return ''

        try:
            return _grant_new_lock(filepath)
        except Exception as e:
            #logging.exception(e)
            raise web.unauthorized()


    def DELETE(self, filepath):

        web.header('Content-Type', 'text/plain; charset=UTF-8')

        filepath = str(filepath)
        i = web.input()

        if filepath == '/':
            return ''
        elif filepath in _locks:
            raise web.badrequest()
        else:
            return 'OK'


def _lock_expired(filepath):
    #Returns True if the lock of filepath has expired

    return ''


def _grant_new_lock(filepath):
    #Grant a new lock and return its id

    if filepath in _locks:
        _revoke_lock(filepath)
    return _new_lock(filepath)


def _new_lock(filepath):
    #Create a new lock for filepath, and return its id

    lock_id = random.randrange(0, 35000)
    logging.info('Granting lock (%d) on %s.', lock_id, filepath)
    t = datetime.datetime.now()
    _locks[filepath] = Lock(lock_id, t, t)

    return lock_id


def _update_lock(filepath):
    #Update the last_used fields of locks to now

    t = datetime.datetime.now() #update time

    #logging.info('Update lock on %s from %s to %s.',filepath, _locks[filepath].last_used, t)

    l = _locks[filepath]
    l = Lock(l.lock_id, l.granted, t)
    _locks[filepath] = l


def _revoke_lock(filepath):
    #Revoke the lock

    if filepath in _locks:
        #logging.info('Revoking lock on %s.', filepath)
        del _locks[filepath]


_config = {
            'dbfile': 'locks.db',
            'lock_lifetime': 60,
         }

logging.info('Loading config file lockserver.dfs.json.')
_locks = shelve.open(_config['dbfile'])

atexit.register(lambda: _locks.close())
