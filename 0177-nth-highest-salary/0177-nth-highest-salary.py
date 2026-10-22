import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=["salary"])
    if ((employee["salary"].nunique() < N) or (N<1)): 
        return pd.DataFrame({f"getNthHighestSalary({N})":[None]})
    return pd.DataFrame({f"getNthHighestSalary({N})":[employee.sort_values("salary", ascending=False).iloc[N-1]["salary"]]})
    