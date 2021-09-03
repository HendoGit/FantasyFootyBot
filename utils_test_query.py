import pandas as pd


from sqlalchemy import create_engine

import json

with open('credentials.json') as f:
  credentials = json.load(f)

end_point = 'alex-aicore.c36j3dhgfor3.eu-west-2.rds.amazonaws.com'
port = '5432'
db_identifier = 'postgres'
database_connection = create_engine(f'postgresql://postgres:{credentials["password"]}@{end_point}/{db_identifier}').connect()



sql_query='''
SELECT * FROM "LEAGUE_TABLE"

'''
df2=pd.read_sql(sql_query,con=database_connection)


