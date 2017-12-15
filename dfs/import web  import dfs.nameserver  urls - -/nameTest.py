import web, dfs.nameserver

urls = (
        '(/.*)', 'dfs.nameserver.NameServer',
       )

app = web.application(urls, globals())


if __name__ == '__main__':
    app.run()
