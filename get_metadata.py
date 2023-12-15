import argparse
import json
import re

import openreview
from tqdm import tqdm

import config


def init_client(api_version):
    if api_version == "v1":
        return openreview.Client(baseurl="https://api.openreview.net")
    elif api_version == "v2":
        return openreview.api.OpenReviewClient(baseurl='https://api2.openreview.net')
    else:
        raise ValueError(f"Unknown API version: {api_version}")

def get_submissions(client, api_version, invitation):
    if api_version == "v1":
        return openreview.tools.iterget_notes(client, invitation=invitation)
    elif api_version == "v2":
        return client.get_all_notes(invitation=invitation)
    else:
        raise ValueError(f"Unknown API version: {api_version}")

def get_value(x): 
    return x["value"] if isinstance(x, dict) else x

def get_decision(client, paper_number, forum, invitation_template):
    invitation = invitation_template.format(paper_number=paper_number)
    decision = client.get_notes(invitation=invitation, forum=forum)
    import pdb; pdb.set_trace()
    assert len(decision) == 1, f"decision list size: {len(decision)}"
    keys = decision[0].content.keys()
    if "consistency_experiment" in keys:
        d = decision[0].content["consistency_experiment"]
        results = re.findall(r".*This copy’s committee reached the following decision: \*\*(.*)\*\*", d)
        if len(results) == 0:
            results = re.findall(r".*Both committees reached the same decision: \*\*(.*)\*\*", d)
        assert len(results) == 1, f"results list size: {len(results)}, {forum}, {d}"
        return results[0]
    elif "decision" in keys:
        return decision[0].content["decision"]
    elif "recommendation" in keys:
        return decision[0].content["recommendation"]
    else:
        raise RuntimeError("Unable to parse decision:", decision[0])
    

def get_ratings(client, paper_number, invitation_template, rating_parser=None):
    invitation = invitation_template.format(paper_number=paper_number)
    ratings = client.get_notes(invitation=invitation)
    keys = ratings[0].content.keys()
    rating_keys = ["rating", "recommendation"]
    key = None
    for k in rating_keys:
        if k in keys:
            key = k
            break
    if key is None:
        raise ValueError(f"Rating not found: {keys}")
    ratings = [r.content[key] for r in ratings]
    if rating_parser is not None:
        ratings = [rating_parser(r) for r in ratings]
    return ratings

def get_tldr(x):
    keys = ["TL;DR", "TLDR", "one-sentence_summary"]
    for k in keys:
        if k in x:
            r = x[k]
            r = get_value(r)
            return r

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("conference", help="conference key from config.py")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    
    outpath = f"data/{args.conference}.json"
    data = []
    cfgs = config.cfg[args.conference]
    
    for cfg in cfgs:
        api_version = cfg.get("api_version", "v1")
        inv_submissions = cfg["inv_submissions"]
        inv_decision_template = cfg["inv_decision_template"]
        inv_ratings_template = cfg["inv_ratings_template"]
        rating_parser = cfg.get("rating_parser", None)
        decision_parser = cfg.get("decision_parser", None)
        client = init_client(api_version)
        submissions = get_submissions(client, api_version, inv_submissions)
        for subm in tqdm(submissions):
            datum = {
                "id": subm.id,
                "number": subm.number,
                "forum": subm.forum,
                "title": get_value(subm.content["title"]),
                "authors": get_value(subm.content["authors"]),
                "abstract": get_value(subm.content["abstract"]),
                "code": get_value(subm.content.get("code", None)),
                "keywords": get_value(subm.content.get("keywords", None)),
            }
            datum["tldr"] = get_tldr(subm.content)
            datum["ratings"] = get_ratings(client, subm.number, inv_ratings_template, rating_parser)
            if decision_parser is not None:
                datum["decision"] = decision_parser(subm)
            else:
                datum["decision"] = get_decision(client, subm.number, subm.forum, inv_decision_template)
            data.append(datum)

    with open(outpath, "w", encoding="utf-8") as ff:
        json.dump(data, ff, indent=4)