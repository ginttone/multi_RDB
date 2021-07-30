import sqlite3
connect = sqlite3.connect('../db.sqlite3')

import pandas as pd
df = pd.read_sql_query("select * from polls_economics where title like '%마스크%'",connect)


connect.close()