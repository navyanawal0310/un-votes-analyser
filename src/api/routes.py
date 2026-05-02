from fastapi import APIRouter, HTTPException
from src.analysis.stance import country_issue_stance, dominant_stance
from src.analysis.alignment import country_alignment
from src.analysis.global_analysis import global_issue_distribution

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
def global_issue(issue: str):
    df = global_issue_distribution(issue)

    if df.empty:
        raise HTTPException(status_code=404, detail="Issue not found")

    return {
        "issue": issue,
        "distribution": df.to_dict(orient="records")
    }