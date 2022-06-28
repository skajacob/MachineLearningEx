import mysql.connector as sql
import pandas as pd

db_connect=sql.connect(host='localhost', database='test', user='root', password = '')
df = pd.read_sql('SELECT * FROM user_details', con=db_connect)
df.head()