import glob
import json
import os

import numpy as np
import pandas as pd

def preprocess(x):
    # let's show only accepted papers
    df = pd.DataFrame(x)
    df = df[df["decision"] != "Reject"]

    # calc avg rating and sort by it
    first_rating = df["ratings"].iloc[0][0]
    is_rating_numeric = isinstance(first_rating, int)
    if is_rating_numeric:
        df["ratings_numeric"] = df["ratings"]
    else:
        df["ratings_numeric"] = df["ratings"].apply(lambda x: [int(xx.split(":")[0]) for xx in x])
    min_num_ratings = df["ratings_numeric"].apply(len).min()
    assert min_num_ratings > 0, f"min_num_ratings: {min_num_ratings}"
    df["avg_rating"] = df["ratings_numeric"].apply(lambda x: np.mean(x))
    df = df.sort_values("avg_rating", ascending=False)

    # check if paper was assigned to multiple review committees
    # if yes, remove the duplicate but add rating2, id2 fields
    # also, add ranking field
    done = set()
    values = []
    cnt = 0
    for i, row in df.iterrows():
        vals = row.to_dict()
        vals["ranking"] = cnt + 1
        
        title = row.title
        if title in done:
            continue
        df_sub = df[df["title"] == title]
        assert len(df_sub) <= 2
        if len(df_sub) == 2:
            row2 = df_sub.iloc[1]
            vals["ratings_numeric2"] = row2["ratings_numeric"]
            vals["avg_rating2"] = row2["avg_rating"]
            vals["decision2"] = row2["decision"]
            vals["id2"] = row2["id"]

        cnt += 1
        done.add(title)
        values.append(vals)
    
    return values

def split_conf_name_year(x):
    name = x[:-4]
    year = x[-4:]
    return name, year

def beautify_conf_name(x):
    if x == "neurips":
        return "NeurIPS"
    else:
        return x.upper()

def beautify_conf_name_year(x):
    name, year = split_conf_name_year(x)
    name = beautify_conf_name(name)
    name = name + " " + year
    return name

def load_data():
    papers_data = {}
    files = sorted(glob.glob("data/*.json"))
    for f in files:
        with open(f) as ff:
            data = json.load(ff)
        confname = os.path.basename(f).replace(".json", "")
        papers_data[confname] = preprocess(data)

    confs_data = {}
    for k in papers_data.keys():
        name, year = split_conf_name_year(k)
        if name in confs_data:
            confs_data[name]["years"].append(year)
        else:
            confs_data[name] = {"name": beautify_conf_name(name), "years": [year]}
    for k, v in confs_data.items():
        confs_data[k]["years"] = sorted(v["years"], reverse=True)

    
    return papers_data, confs_data