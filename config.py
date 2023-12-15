cfg = {}

# NeurIPS
def neurips2023_decision_parser(x):
    return {
        "NeurIPS 2023 poster": "Poster",
        "NeurIPS 2023 spotlight": "Spotlight",
        "Submitted to NeurIPS 2023": "Reject",
        "NeurIPS 2023 oral": "Oral",
        "NeurIPS 2023 Datasets and Benchmarks Poster": "Poster",
        "NeurIPS 2023 Datasets and Benchmarks Spotlight": "Spotlight",
        "Submitted to NeurIPS 2023 Datasets and Benchmarks": "Reject",
        "NeurIPS 2023 Datasets and Benchmarks Oral": "Oral",
    }.get(x.content["venue"]["value"])

cfg = {
    "neurips2021": [
        {
            "inv_submissions": "NeurIPS.cc/2021/Conference/-/Blind_Submission",
            "inv_decision_template": "NeurIPS.cc/2021/Conference/Paper{paper_number}/-/Decision",
            "inv_ratings_template": "NeurIPS.cc/2021/Conference/Paper{paper_number}/-/Official_Review",
            "name": "NeurIPS 2021",
        },
        {
            "inv_submissions": "NeurIPS.cc/2021/Track/Datasets_and_Benchmarks/Round1/-/Submission",
            "inv_decision_template": "NeurIPS.cc/2021/Track/Datasets_and_Benchmarks/Round1/Paper{paper_number}/-/Decision",
            "inv_ratings_template": "NeurIPS.cc/2021/Track/Datasets_and_Benchmarks/Round1/Paper{paper_number}/-/Official_Review",
            "name": "NeurIPS 2021",
        },
        {
            "inv_submissions": "NeurIPS.cc/2021/Track/Datasets_and_Benchmarks/Round2/-/Submission",
            "inv_decision_template": "NeurIPS.cc/2021/Track/Datasets_and_Benchmarks/Round2/Paper{paper_number}/-/Decision",
            "inv_ratings_template": "NeurIPS.cc/2021/Track/Datasets_and_Benchmarks/Round2/Paper{paper_number}/-/Official_Review",
            "name": "NeurIPS 2021",
        },
    ],
    "neurips2022": [
        {
            "inv_submissions": "NeurIPS.cc/2022/Conference/-/Blind_Submission",
            "inv_decision_template": "NeurIPS.cc/2022/Conference/Paper{paper_number}/-/Decision",
            "inv_ratings_template": "NeurIPS.cc/2022/Conference/Paper{paper_number}/-/Official_Review",
            "name": "NeurIPS 2022",
        },
        {
            "inv_submissions": "NeurIPS.cc/2022/Track/Datasets_and_Benchmarks/-/Submission",
            "inv_decision_template": "NeurIPS.cc/2022/Track/Datasets_and_Benchmarks/Paper{paper_number}/-/Decision",
            "inv_ratings_template": "NeurIPS.cc/2022/Track/Datasets_and_Benchmarks/Paper{paper_number}/-/Official_Review",
            "name": "NeurIPS 2022",
        },
    ],
    "neurips2023": [
        {
            "inv_submissions": "NeurIPS.cc/2023/Conference/-/Submission",
            "inv_decision_template": None,
            "inv_ratings_template": "NeurIPS.cc/2023/Conference/Submission{paper_number}/-/Official_Review",
            "name": "NeurIPS 2023",
            "api_version": "v2",
            "rating_parser": lambda x: x["value"].split(":")[0],
            "decision_parser": neurips2023_decision_parser,
        },
        {
            "inv_submissions": "NeurIPS.cc/2023/Track/Datasets_and_Benchmarks/-/Submission",
            "inv_decision_template": None,
            "inv_ratings_template": "NeurIPS.cc/2023/Track/Datasets_and_Benchmarks/Submission{paper_number}/-/Official_Review",
            "name": "NeurIPS 2023",
            "api_version": "v2",
            "rating_parser": lambda x: x["value"].split(":")[0],
            "decision_parser": neurips2023_decision_parser,
        },
    ],
}

# ICLR
cfg["iclr2023"] = [
    {
        "inv_submissions": "ICLR.cc/2023/Conference/-/Blind_Submission",
        "inv_decision_template": "ICLR.cc/2023/Conference/Paper{paper_number}/-/Decision",
        "inv_ratings_template": "ICLR.cc/2023/Conference/Paper{paper_number}/-/Official_Review",
        "name": "ICLR 2023",
    },
]

cfg["iclr2022"] = [
    {
        "inv_submissions": "ICLR.cc/2022/Conference/-/Blind_Submission",
        "inv_decision_template": "ICLR.cc/2022/Conference/Paper{paper_number}/-/Decision",
        "inv_ratings_template": "ICLR.cc/2022/Conference/Paper{paper_number}/-/Official_Review",
        "name": "ICLR 2022",
    },
]

cfg["iclr2021"] = [
    {
        "inv_submissions": "ICLR.cc/2021/Conference/-/Blind_Submission",
        "inv_decision_template": "ICLR.cc/2021/Conference/Paper{paper_number}/-/Decision",
        "inv_ratings_template": "ICLR.cc/2021/Conference/Paper{paper_number}/-/Official_Review",
        "name": "ICLR 2021",
    },
]

cfg["iclr2020"] = [
    {
        "inv_submissions": "ICLR.cc/2020/Conference/-/Blind_Submission",
        "inv_decision_template": "ICLR.cc/2020/Conference/Paper{paper_number}/-/Decision",
        "inv_ratings_template": "ICLR.cc/2020/Conference/Paper{paper_number}/-/Official_Review",
        "name": "ICLR 2020",
    },
]

cfg["iclr2019"] = [
    {
        "inv_submissions": "ICLR.cc/2019/Conference/-/Blind_Submission",
        "inv_decision_template": "ICLR.cc/2019/Conference/-/Paper{paper_number}/Meta_Review",
        "inv_ratings_template": "ICLR.cc/2019/Conference/-/Paper{paper_number}/Official_Review",
        "name": "ICLR 2019",
    },
]

cfg["iclr2018"] = [
    {
        "inv_submissions": "ICLR.cc/2018/Conference/-/Blind_Submission",
        "inv_decision_template": "ICLR.cc/2018/Conference/-/Acceptance_Decision",
        "inv_ratings_template": "ICLR.cc/2018/Conference/-/Paper{paper_number}/Official_Review",
        "name": "ICLR 2018",
    },
]

cfg["iclr2017"] = [
    {
        "inv_submissions": "ICLR.cc/2017/conference/-/submission",
        "inv_decision_template": "ICLR.cc/2017/conference/-/paper{paper_number}/acceptance",
        "inv_ratings_template": "ICLR.cc/2017/conference/-/paper{paper_number}/official/review",
        "name": "ICLR 2017",
    },
]