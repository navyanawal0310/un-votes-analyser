import pandas as pd

def clean_votes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Rename columns to standard names
    df = df.rename(columns={
        "ms_name": "country",
        "ms_vote": "vote",
        "resolution": "resolution_id",
        "date": "date",
        "subjects": "subjects",
        "agenda_title": "agenda",
        "title": "title"
    })

    # Standardize vote values
    vote_map = {
        "Y": "YES",
        "N": "NO",
        "A": "ABSTAIN",
        "9": "ABSENT"  # sometimes appears
    }
    df["vote"] = df["vote"].map(vote_map)

    # Convert date → year
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year"] = df["date"].dt.year

    # Drop invalid rows
    df = df.dropna(subset=["country", "vote", "resolution_id"])

    # Keep only relevant columns
    df = df[[
        "country",
        "resolution_id",
        "vote",
        "year",
        "subjects",
        "agenda",
        "title"
    ]]

    return df