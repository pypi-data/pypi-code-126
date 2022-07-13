# -*- coding: utf-8 -*-
import sys
import logging

from .dir_clean import main

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(name)s : %(levelname)s : %(message)s', level=logging.INFO)

    ret = main()
    sys.exit(ret)
