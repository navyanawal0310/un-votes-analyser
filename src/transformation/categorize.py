import pandas as pd

def extract_main_issue(subject):
    if pd.isna(subject):
        return "OTHER"

    subject = subject.lower()

    if "nuclear" in subject or "disarmament" in subject:
        return "NUCLEAR"
    elif "palestine" in subject or "middle east" in subject:
        return "MIDDLE_EAST"
    elif "human rights" in subject:
        return "HUMAN_RIGHTS"
    elif "climate" in subject or "environment" in subject:
        return "CLIMATE"
    else:
        return "OTHER"