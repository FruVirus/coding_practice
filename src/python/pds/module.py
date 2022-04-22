# pylint: disable=C0114, E1121, R0204

# Third Party Library
import pandas as pd

# Pandas Tutorial #

# Pandas Getting Started
print(pd.__version__)
mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
myvar = pd.DataFrame(mydataset)
print(myvar)
print()

# Pandas Series
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])
print(myvar[1])
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
myvar = pd.DataFrame(data)
print(myvar)
print()

# Pandas DataFrames
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[[0, 1]])
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
print(df.loc["day2"])
print()

# Pandas Read CSV
fp = "/home/zhen/Projects/personal/coding_practice/src/python/pds/data.csv"
df = pd.read_csv(fp)
print(df.to_string())
df = pd.read_csv(fp)
print(df)
print(pd.options.display.max_rows)
pd.options.display.max_rows = 9999
print(df)
print()

# Pandas Read JSON
fp = "/home/zhen/Projects/personal/coding_practice/src/python/pds/data.json"
df = pd.read_json(fp)
print(df.to_string())
print()

# Pandas Analyzing Data
fp = "/home/zhen/Projects/personal/coding_practice/src/python/pds/data.csv"
df = pd.read_csv(fp)
print(df.head(10))
print(df.tail())
print(df.info())
print()

# Cleaning Data #

# Cleaning Empty Cells
fp = "/home/zhen/Projects/personal/coding_practice/src/python/pds/dirtydata.csv"
df = pd.read_csv(fp)
new_df = df.dropna()
print(new_df.to_string())
df = pd.read_csv(fp)
df.dropna(inplace=True)
print(df.to_string())
df = pd.read_csv(fp)
df.fillna(130, inplace=True)
print(df.to_string())
df = pd.read_csv(fp)
df["Calories"].fillna(130, inplace=True)
print(df.to_string())
df = pd.read_csv(fp)
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace=True)
print(df.to_string())
df = pd.read_csv(fp)
x = df["Calories"].median()
df["Calories"].fillna(x, inplace=True)
df = pd.read_csv(fp)
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)
print(df.to_string())
print()

# Cleaning Wrong Format
fp = "/home/zhen/Projects/personal/coding_practice/src/python/pds/dirtydata.csv"
df = pd.read_csv(fp)
df["Date"] = pd.to_datetime(df["Date"])
print(df.to_string())
df.dropna(subset=["Date"], inplace=True)
print(df.to_string())
print()

# Cleaning Wrong Data
fp = "/home/zhen/Projects/personal/coding_practice/src/python/pds/dirtydata.csv"
df = pd.read_csv(fp)
df.loc[7, "Duration"] = 45
print(df.to_string())
df = pd.read_csv(fp)
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
print(df.to_string())
df = pd.read_csv(fp)
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)
print(df.to_string())
print()

# Removing Duplicates
fp = "/home/zhen/Projects/personal/coding_practice/src/python/pds/dirtydata.csv"
df = pd.read_csv(fp)
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df.to_string())
print()

# Correlations #

# Pandas Correlations
fp = "/home/zhen/Projects/personal/coding_practice/src/python/pds/data.csv"
df = pd.read_csv(fp)
print(df.corr())
print()
