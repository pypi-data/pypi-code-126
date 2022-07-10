import poker_log_parser as pklp
import time
import os
import pprint

if __name__ == '__main__':
    root = 'C:\\Users\\Djordje\\Desktop\\projects\\poker-log-parser\\tests\\data\\PokerStars'
    paths = [f'{root}\\{f}' for f in os.listdir(root)]
    now = time.time()
    r = pklp.parse_paths(paths)
    taken = time.time()-now
    total = sum([len(x) for x in r])
    print(f'Took {taken:.2f}s hands/sec: {total/taken:.2f}')

