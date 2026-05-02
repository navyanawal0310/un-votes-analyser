import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw/un_votes.csv")

def load_data(sample=False):
    if sample:
        # Load only first 10k rows for testing
        df = pd.read_csv(RAW_DATA_PATH, nrows=10000)
    else:
        # Load in chunks
        chunks = []
        for chunk in pd.read_csv(RAW_DATA_PATH, chunksize=50000):
            chunks.append(chunk)
        df = pd.concat(chunks, ignore_index=True)

    print("Data loaded successfully")
    print(df.shape)
    print(df.columns)

    return df

if __name__ == "__main__":
    load_data(sample=True)