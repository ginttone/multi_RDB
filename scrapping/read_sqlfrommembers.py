#db에서 데이터 불러오기

import sqlite3
connect = sqlite3.connect('../db.sqlite3')

import pandas as pd
#sql_query 테이블 안에 건드리는 쿼리문(시퀄) 사용
df = pd.read_sql_query('select * from members where age>=30',connect)

connect.close()
