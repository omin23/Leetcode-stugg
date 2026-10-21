import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    smth = person.groupby("email").count().reset_index()
    return smth[smth["id"]>1][["email"]]
