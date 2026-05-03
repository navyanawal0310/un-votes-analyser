from fastapi import APIRouter, HTTPException
from src.analysis.stance import country_issue_stance, dominant_stance
from src.analysis.alignment import country_alignment
from src.analysis.global_analysis import global_issue_distribution
from src.ingestion.load_un_data import load_data
import pandas as pd

router = APIRouter()

@router.get("/country/{country}")
def get_country_stance(country: str):
    df = country_issue_stance(country)

    if df.empty:
        raise HTTPException(status_code=404, detail="Country not found")

    return {
        "country": country,
        "stance": df.reset_index().to_dict(orient="records"),
        "dominant": dominant_stance(df)
    }


@router.get("/compare/{country1}/{country2}")
def compare_countries(country1: str, country2: str):
    score = country_alignment(country1, country2)

    return {
        "country1": country1,
        "country2": country2,
        "alignment_score": score
    }


@router.get("/global/{issue}")
def global_issue_distribution(issue: str):
    df = load_data()

    # ✅ STEP 1: Filter first
    df_filtered = df[
        df["subjects"]
        .fillna("")
        .astype(str)
        .str.lower()
        .str.contains(issue.lower(), na=False)
    ]

    # ✅ STEP 2: Map vote labels
    vote_map = {
        "Y": "YES",
        "N": "NO",
        "A": "ABSTAIN",
        "X": "ABSENT"
    }

    df_filtered["vote_label"] = df_filtered["ms_vote"].map(vote_map)

    # ✅ STEP 3: Count using mapped values
    vote_counts = df_filtered["vote_label"].value_counts().to_dict()

    return {
        "issue": issue,
        "distribution": vote_counts
    }