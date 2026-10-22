import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(["recordDate"], inplace=True)
    prevd = (weather["recordDate"] - weather["recordDate"].shift(1)).dt.days == 1 
    return weather[(weather["temperature"] > weather["temperature"].shift(1)) & prevd][["id"]]
    
    