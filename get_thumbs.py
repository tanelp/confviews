import argparse
import json
import os
import urllib.request

from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("conference", help="conference key from config.py")
    args = parser.parse_args()
    return args

def download_pdf(paperid, outpath="temp.pdf"):
    url = f"https://openreview.net/pdf?id={paperid}"
    urllib.request.urlretrieve(url, outpath)
    return outpath

def create_thumb(pdfpath, thumbpath):
    cmd = f"montage {pdfpath}[0-7] -mode Concatenate -tile x1 -quality 80 -resize x230 -trim -colorspace rgb {thumbpath}"
    os.system(cmd)

def do_process(x):
    return x["decision"] != "Reject"

if __name__ == "__main__":
    args = parse_args()

    metapath = f"data/{args.conference}.json"
    with open(metapath) as ff:
        data = json.load(ff)

    for x in tqdm(data):
        if do_process(x):
            id_ = x["forum"]
            thumbdir = os.path.join("static", args.conference, "thumbs")
            os.makedirs(thumbdir, exist_ok=True)
            thumbpath = os.path.join(thumbdir, f"{id_}.jpg")
            if not os.path.exists(thumbpath):
                try:
                    pdfpath = download_pdf(id_)
                    create_thumb(pdfpath, thumbpath)
                except Exception as e:
                    print(id_)
                    print(e)
    
