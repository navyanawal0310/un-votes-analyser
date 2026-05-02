import pandas as pd
from src.utils.db import engine


def country_issue_stance(country):
    query = """
        SELECT 
            i.issue_name,
            f.vote,
            COUNT(*) as vote_count
        FROM fact_votes f
        JOIN dim_countries c ON f.country_id = c.country_id
        JOIN dim_issues i ON f.issue_id = i.issue_id
        WHERE LOWER(c.country_name) = LOWER(%s)
        GROUP BY i.issue_name, f.vote
    """
    df = pd.read_sql(query, engine, params=(country,))
    if df.empty:
        return df
    pivot = df.pivot(index="issue_name", columns="vote", values="vote_count").fillna(0)
    pct = pivot.div(pivot.sum(axis=1), axis=0) * 100
    return pct.round(1)

def dominant_stance(df):
    result = {}
    for issue in df.index:
        top_vote = df.loc[issue].idxmax()
        result[issue] = top_vote
    return result