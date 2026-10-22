import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers.drop_duplicates(subset=["num"],keep=False, inplace=True)
    if my_numbers["num"].empty:return pd.DataFrame({"num":[np.nan]})
    else:return my_numbers.sort_values("num", ascending=False).head(1)