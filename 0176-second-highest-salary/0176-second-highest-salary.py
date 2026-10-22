import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if employee["salary"].nunique() < 2: return pd.DataFrame({"SecondHighestSalary":[None]})
    employee = employee.drop_duplicates(subset="salary").sort_values("salary", ascending=False)
    return pd.DataFrame({"SecondHighestSalary":[employee.iloc[1,1]]})