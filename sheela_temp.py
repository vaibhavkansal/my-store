import pandas as pd
df=pd.read_csv("sheela.csv")
df['vwdtc']= pd.to_datetime(df['vwdtc'], format='%d/%m/%y')
df.to_csv("new_temp.csv")
