import pandas as pd
import numpy as np

data=pd.read_csv("./results.csv",sep=",")
SMN=data["home_team"]=="San Marino"
home_win=data["home_score"]>data["away_score"]
print(data[SMN & home_win])
