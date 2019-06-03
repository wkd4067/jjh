# 시간에 따른 각 범죄 유형의 발생 횟수 비교

학과 | 학번 | 성명
---- | ---- | ---- 
통계학과 |201511538 |정장현


## 프로젝트 개요
강력범죄, 절도범죄, 폭력범죄의 시간별 발생횟수의 평균을 구하고 그에 따른 그래프를 그려 비교한다.

## 사용한 공공데이터 
[데이터보기](https://github.com/cybermin/python2019/blob/master/%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EB%8F%84%EC%8B%9C%EC%B2%A0%EB%8F%84%EC%97%AD%EC%82%AC%EC%A0%95%EB%B3%B4_20190520.csv)

## 소스
* [링크로 소스 내용 보기](https://github.com/cybermin/python2019/blob/master/tes.py) 

* 코드 삽입
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

print(df4)

df4.plot(kind='bar')

![1111](https://user-images.githubusercontent.com/51112537/58796500-66a6aa80-8638-11e9-8e71-1e4eb16908eb.PNG)



print(df6)

df6.plot(kind='bar')

![2222](https://user-images.githubusercontent.com/51112537/58796568-95bd1c00-8638-11e9-886b-ed11b69e8a25.PNG)


print(df7)
df7.plot(kind='bar')

![3333](https://user-images.githubusercontent.com/51112537/58796588-a40b3800-8638-11e9-8d5a-c27edd039069.PNG)



