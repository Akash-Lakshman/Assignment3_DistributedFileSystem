import web, utils, atexit, logging, os, shelve

class NameServer:

    def GET(self, filepath):
     
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        filepath = str(filepath)

        if filepath == '/':
            return '\n'.join('%s=%s' % (dirpath, _names[dirpath])
                    for dirpath in sorted(_names))

        dirpath = str(os.path.dirname(filepath))

        if dirpath in _names:
            return _names[dirpath]

        raise web.notfound('No file server serve this file.')


    def POST(self, dirpath):
        """See _update (with add=True)."""

        return _update(str(dirpath))

    def DELETE(self, dirpath):
        """See _update (with add=False)."""

        return _update(str(dirpath), False)


def _update(dirpath, add=True):
       
    web.header('Content-Type', 'text/plain; charset=UTF-8')
    i = web.input()

    if 'srv' not in i:
        raise web.badrequest()

    srv = i['srv']

    if dirpath == '/':
        if 'dirs' not in i:
            raise web.badrequest()

        for dirpath in i['dirs'].split('\n'):
            if not dirpath:
                continue

            try:
                _update_names(dirpath, srv, add)
            except ValueError as e:
                logging.exception(e)

    else:
        try:
            _update_names(dirpath, srv, add)
        except ValueError as e:
            logging.exception(e)

    return 'OK'


def _update_names(dirpath, srv, add=True):

    if dirpath[-1] == '/':
        dirpath = os.path.dirname(dirpath)

    if add:
        logging.info('Update directory %s on %s.', dirpath, srv)
        _names[dirpath] = srv

    elif dirpath in _names:
        logging.info('Remove directory %s on %s.', dirpath, srv)
        del _names[dirpath]

    else:
        raise ValueError('%s wasn\'t not deleted, because it wasn\'t'
                         ' in the dictionnary/database.' % dirpath)


_config = {
            'dbfile': 'names.db',
         }

logging.info('Loading config file nameserver.dfs.json.')
utils.load_config(_config, 'nameserver.dfs.json')
_names = shelve.open(_config['dbfile'])

atexit.register(lambda: _names.close())
