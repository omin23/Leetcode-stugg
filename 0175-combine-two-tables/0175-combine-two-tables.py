import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    tgt = pd.merge(person,address, on="personId", how="left")
    return tgt[["firstName","lastName","city","state"]]
    