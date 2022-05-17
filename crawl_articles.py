#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The GermanFakeNC dataset does not include articles itself, just their URLs
# This script is for following those URLs to retrieve the actual texts

import json
from newspaper import Article

title_text_list = []
defective_entries = []
valid_entries = []
with open("datasets/GermanFakeNC.json","r",encoding="utf-8") as original_file:
    data = json.load(original_file)
    for entry in data:
        url = entry["URL"]
        article = Article(url,language="de")
        try:
            article.download()
            article.parse()
        except:
            defective_entries.append(entry)
        else:
            valid_entries.append(entry)
            title_text_list.append({"title":article.title,"text":article.text})


with open(r"datasets/texts_GermanFakeNC.json","w",encoding="utf-8") as f:
    json.dump(title_text_list,f,ensure_ascii=False,indent=4)

with open(r"datasets/INVALIDS_GermanFakeNC.json","w",encoding="utf-8") as f:
    json.dump(defective_entries,f,ensure_ascii=False,indent=4)

with open(r"datasets/VALIDS_GermanFakeNC.json","w",encoding="utf-8") as f:
    json.dump(valid_entries,f,ensure_ascii=False,indent=4)