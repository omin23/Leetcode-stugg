import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    sal_map = employee.set_index("id")["salary"]
    employee["msal"] = employee["managerId"].map(sal_map)
    res = employee["salary"] > employee["msal"]
    return employee[res][["name"]].rename(columns={"name":"Employee"})