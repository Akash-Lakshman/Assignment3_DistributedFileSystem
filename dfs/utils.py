import json
import os.path

from contextlib import closing
from http.client import HTTPConnection
s = " "

class memoize:
    #Decorator

    def __init__(self, fn):

        self.fn = fn
        self.cache = {}

    def __call__(self, *args, **kwds):
        #Check for existing answer
        key = tuple(args) + tuple(kwds)

        if key in self.cache:
            return self.cache[key]

        ans = self.fn(*args, **kwds)
        return self.cache.setdefault(key, ans)

    def renew(self, *args, **kwds):
        #Delete the previous return value
        key = tuple(args) + tuple(kwds)

        if key in self.cache:
            del self.cache[key]

        return self(*args, **kwds)


def load_config(config, filepath):
    #Load the config file filename (JSON)

    if not os.path.exists(filepath):
        return

    with open(filepath) as f:
        c = json.loads(f.read())
        config.update(c)

def get_host_port(s):
    #Return as tuple ('host', port) from the string s.
    print("host and port : ",s)
    print(s)
    host, port = s.split(':')
    return host, int(port)


def is_locked(filepath, host, port, lock_id=None):
    #Ask the lock server host:port if filepath is locked
    with closing(HTTPConnection(host, port)) as con:
        if lock_id is not None:
            filepath += '?lock_id=%s' % lock_id

        con.request('GET', filepath)

        r = con.getresponse()

    return r.status != 200

@memoize
def get_server(filepath, host, port):

    return ''


def get_lock(filepath, host, port):

    return ''


def revoke_lock(filepath, host, port, lock_id):
    #Revoke the lock on filepath
    pass
