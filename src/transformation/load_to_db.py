import pandas as pd
from sqlalchemy import text
from src.utils.db import engine


def load_dimensions(df):
    with engine.begin() as conn:

        # Countries
        countries = df[["country"]].drop_duplicates()
        countries.columns = ["country_name"]

        for _, row in countries.iterrows():
            conn.execute(
                text("""
                INSERT INTO dim_countries (country_name)
                VALUES (:country)
                ON CONFLICT (country_name) DO NOTHING
                """),
                {"country": row["country_name"]}
            )

        # Issues
        issues = df[["issue"]].drop_duplicates()
        issues.columns = ["issue_name"]

        for _, row in issues.iterrows():
            conn.execute(
                text("""
                INSERT INTO dim_issues (issue_name)
                VALUES (:issue)
                ON CONFLICT (issue_name) DO NOTHING
                """),
                {"issue": row["issue_name"]}
            )

        # Resolutions
        resolutions = df[["resolution_id", "title", "agenda", "year"]].drop_duplicates()

        for _, row in resolutions.iterrows():
            conn.execute(
                text("""
                INSERT INTO dim_resolutions (resolution_id, title, agenda, year)
                VALUES (:rid, :title, :agenda, :year)
                ON CONFLICT (resolution_id) DO NOTHING
                """),
                {
                    "rid": row["resolution_id"],
                    "title": row["title"],
                    "agenda": row["agenda"],
                    "year": row["year"]
                }
            )


def load_fact(df):
    with engine.begin() as conn:

        for _, row in df.iterrows():
            conn.execute(
                text("""
                INSERT INTO fact_votes (country_id, resolution_id, issue_id, vote, year)
                SELECT 
                    c.country_id,
                    :resolution_id,
                    i.issue_id,
                    :vote,
                    :year
                FROM dim_countries c, dim_issues i
                WHERE c.country_name = :country
                AND i.issue_name = :issue
                """),
                {
                    "country": row["country"],
                    "issue": row["issue"],
                    "resolution_id": row["resolution_id"],
                    "vote": row["vote"],
                    "year": row["year"]
                }
            )


def load_all(df):
    load_dimensions(df)
    load_fact(df)