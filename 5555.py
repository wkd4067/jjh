# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df=pd.read_csv("C:\\Users\\정장현\\Desktop\\범죄발생시간.csv",encoding='euc-kr')
df['00:00-02:59'] = pd.to_numeric(df['00:00-02:59'], errors='coerce').fillna(0)
df['03:00-05:59'] = pd.to_numeric(df['03:00-05:59'], errors='coerce').fillna(0)
df['06:00-08:59'] = pd.to_numeric(df['06:00-08:59'], errors='coerce').fillna(0)
df['09:00-11:59'] = pd.to_numeric(df['09:00-11:59'], errors='coerce').fillna(0)
df['12:00-14:59'] = pd.to_numeric(df['12:00-14:59'], errors='coerce').fillna(0)
df['15:00-17:59'] = pd.to_numeric(df['15:00-17:59'], errors='coerce').fillna(0)
df['18:00-20:59'] = pd.to_numeric(df['18:00-20:59'], errors='coerce').fillna(0)
df['21:00-23:59'] = pd.to_numeric(df['21:00-23:59'], errors='coerce').fillna(0)

df1=df.loc[0:7,['범죄대분류','00:00-02:59','03:00-05:59','06:00-08:59','09:00-11:59','12:00-14:59','15:00-17:59','18:00-20:59','21:00-23:59']]
df2=df.loc[8,['범죄대분류','00:00-02:59','03:00-05:59','06:00-08:59','09:00-11:59','12:00-14:59','15:00-17:59','18:00-20:59','21:00-23:59']]
df3=df.loc[9:16,['범죄대분류','00:00-02:59','03:00-05:59','06:00-08:59','09:00-11:59','12:00-14:59','15:00-17:59','18:00-20:59','21:00-23:59']]
df4=df1.mean(axis=0)
df5=pd.to_numeric(df2,errors='coerce')
df6=df5.iloc[1:9]
df7=df3.mean(axis=0)
print(df7)
df7.plot(kind='bar')





