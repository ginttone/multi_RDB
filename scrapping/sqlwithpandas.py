#1. 데이터를 db에 넣기
#sklearn에서 dataset 가져와서
from sklearn import datasets
boston = datasets.load_boston()

#dataset을 pandas로 변형
import pandas as pd
df = pd.DataFrame(boston['data'],columns=boston['feature_names'])

#변형된 데이터들을 db에 넣기
import sqlite3
connect = sqlite3.connect('../db.sqlite3')#루트에 있는 db.sqlite3 파일을을열어준다
df.to_sql('boston_table', connect, if_exists='append')#db에 저장하기: to_sql('테이블명')
# if_exists='append' 테이블에 레코드를 계속해서 추가해줄 때 옵션 바꾸기

print(df)
#2. db에서 데이터 불러오기

connect.close()