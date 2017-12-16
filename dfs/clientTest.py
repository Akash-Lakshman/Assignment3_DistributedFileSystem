import random

import dfs.client

if __name__ == '__main__':
    with dfs.client.open('/dt/100', 'a') as f:
        f.write('%6d\n' % random.randint(0, 10 ** 5))

        try:
            open('/dt/100')
        except:
            print('Hell yeah!')
