import pandas as pd


my_data = pd.DataFrame(columns=["Service", "Name", "Password", "Note", "Date", "Salt"])
my_data.to_csv("password_data.csv", sep=",", index=False)