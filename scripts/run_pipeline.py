from src.ingestion.load_un_data import load_data
from src.cleaning.clean_votes import clean_votes
from src.transformation.load_to_db import load_all
from src.transformation.categorize import extract_main_issue

def run_pipeline():
    df = load_data(sample=True)
    df = clean_votes(df)
    df["issue"] = df["subjects"].apply(extract_main_issue)
    df.to_parquet("data/processed/clean_votes.parquet", index=False)
    load_all(df)
    print("Pipeline completed")
    print(df.head())

if __name__ == "__main__":
    run_pipeline()