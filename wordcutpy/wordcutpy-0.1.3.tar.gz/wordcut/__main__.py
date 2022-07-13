import sys
import os.path
from wordcut import Wordcut

def usage():
    print("Usage: python -m wordcut <word list file path>", file=sys.stderr)
    sys.exit(1)

if len(sys.argv) != 2:
    usage()

word_list_file_path = sys.argv[1]

if not os.path.exists(word_list_file_path):
    print(f"{word_list_file_path} does not exist.", file=sys.stderr)
    usage()

with open(word_list_file_path, encoding="UTF-8") as dict_file:
    word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
    wordcut = Wordcut(word_list)
    for line in sys.stdin:
        print("|".join(wordcut.tokenize(line)), end='')
