import pandas as pd

df = pd.read_csv( r'C:\Users\anaik\Desktop\Praca_2021\BitPeak\practise_python_1\todo_list\\' + 'notes.csv', index_col=0)
df.loc[2,:] = ['a','a','a','a','a','a','a']
print(df)