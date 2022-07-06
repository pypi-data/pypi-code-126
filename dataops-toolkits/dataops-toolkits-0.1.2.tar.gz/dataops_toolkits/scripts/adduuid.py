#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataops_toolkits.io import read_json, dump_json
import uuid
import sys


def main():
    data_path = sys.argv[1]
    datas = read_json(data_path)
    if datas is not None:
        new_datas = []
        for data in datas:
            data.update(_id=uuid.uuid4().hex)
            new_datas += [data]

        dump_json(new_datas, data_path)
        print("added!")

    else:
        raise Exception("Invalid Data")


if __name__ == "__main__":
    main()
