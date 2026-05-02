import pandas as pd
from src.utils.db import engine

def country_alignment(country1, country2):
    query = """
        SELECT 
            f1.vote AS vote1,
            f2.vote AS vote2
        FROM fact_votes f1
        JOIN fact_votes f2 
            ON f1.resolution_id = f2.resolution_id
        JOIN dim_countries c1 ON f1.country_id = c1.country_id
        JOIN dim_countries c2 ON f2.country_id = c2.country_id
        WHERE LOWER(c1.country_name) = LOWER(%s)
        AND LOWER(c2.country_name) = LOWER(%s);
    """

    df = pd.read_sql(query, engine, params=(country1, country2))

    if df.empty:
        return 0

    score = 0

    for _, row in df.iterrows():
        if row["vote1"] == row["vote2"]:
            score += 1
        elif "ABSTAIN" in [row["vote1"], row["vote2"]]:
            score += 0.5

    return round(score / len(df), 2)