import pandas as pd

def transform(df:pd.DataFrame):
    df = df.dropna(subset=["userid"])
    df["email"] = df["email"].str.lower()
    df["created_at"] = pd.to_datetime(df["created_at"],utc=True)
    return df