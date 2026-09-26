import pandas as pd

df1 = pd.DataFrame({
    "Id": [1, 2, 3, 4],
    "Name": ["Ram", "Shyam", "Hari", "Sita"]
})

df2 = pd.DataFrame({
    "Id": [3, 4, 5, 6],
    "Marks": [75, 85, 90, 80]
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nInner Join:")
print(pd.merge(df1, df2, on="Id", how="inner"))

print("\nLeft Join:")
print(pd.merge(df1, df2, on="Id", how="left"))

print("\nRight Join:")
print(pd.merge(df1, df2, on="Id", how="right"))

print("\nOuter Join:")
print(pd.merge(df1, df2, on="Id", how="outer"))