import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data, index=['a', 'b', 'c'])
print("Original DataFrame:")
print(df)

    # Reset the index
df_reset = df.reset_index()
print("\nDataFrame after reset_index():")
print(df_reset)