#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This script opens and reads the GermanFakeNC dataset and retrieves all the essential parts of the source 
# URLs. E.g. www.test.com instead of www.test.com/xyz

import json
import re

for file_specifier in ["VALIDS","INVALIDS"]:
    with open("datasets/%s_GermanFakeNC.json"%(file_specifier),
              "r",encoding="utf-8") as file:
        print(file_specifier)
        data = json.load(file)
        print("NUM URLs: "+str(len(data)))
        sources = set()
        for entry in data:
            url = entry["URL"]
            # print(entry["URL"])
            source = re.match(r"((http|https):\/\/)?((\w+\d*\.)?(\w|\d|-)+\.\w+)\/.*",url)
            sources.add(source.group(3))
            # print(source.group(3))
        print("Shortened URLs:")
        print(sources)
        print("NUM SOURCES: "+str(len(sources)))