import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = triangle[["x","y","z"]].sum(axis=1) - 2*triangle[["x","y","z"]].max(axis=1)
    triangle["triangle"] = (triangle["triangle"] > 0).map({False:"No",True:"Yes"})
    # print(triangle)
    return triangle

    