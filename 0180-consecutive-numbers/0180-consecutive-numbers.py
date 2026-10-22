import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs.sort_values("id", inplace=True)
    mask = logs["num"].rolling(3).var() == 0 
    return pd.DataFrame({"ConsecutiveNums": logs["num"][mask].drop_duplicates()})
    
    
    
    