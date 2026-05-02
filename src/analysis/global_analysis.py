import pandas as pd
from src.utils.db import engine


def global_issue_distribution(issue):
    query = f"""
        SELECT 
            f.vote,
            COUNT(*) as count
        FROM fact_votes f
        JOIN dim_issues i ON f.issue_id = i.issue_id
        WHERE i.issue_name = '{issue}'
        GROUP BY f.vote;
    """

    df = pd.read_sql(query, engine)

    return df