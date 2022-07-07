from itertools import cycle

class prox:
    def proxy_format(self, file):
        if os.path.exists(file) == False:
            return 'Provide a valid file.'

        with open(file, 'r') as temp_file:
            try:
                proxy = [line.rstrip('\n') for line in temp_file]
            except:
                return 'The provided file is empty.'

            proxy_pool = cycle(proxy)
            proxy = next(proxy_pool)
            if len(proxy.split(':')) == 4:
                    splitted = proxy.split(':') 
                    return f'http://{splitted[2]}:{splitted[3]}@{splitted[0]}:{splitted[1]}'
                return f'http://{proxy}'