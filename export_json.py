#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import json
import tomllib

DATA_DIR = "./data"


def export():
    cms_list = list()

    # Loop files in data
    for file in os.listdir(DATA_DIR):
        filename = os.fsdecode(file)
        with open(os.path.join(DATA_DIR, filename), "rb") as f:
            try:
                entry = tomllib.load(f)
            except Exception as err:
                raise SystemError(f"Error with #{filename}: #{err}")

            cms_list.append(entry)

    with open("cms.json", "w") as fd:
        json.dump(cms_list, fd)


if __name__ == "__main__":
    try:
        export()
    except Exception as err:
        print(f"[!] #{err}")
