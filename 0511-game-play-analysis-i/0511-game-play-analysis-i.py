import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values("event_date").groupby("player_id").head(1)
    return activity[["player_id","event_date"]].rename(columns={"event_date":"first_login"})


    