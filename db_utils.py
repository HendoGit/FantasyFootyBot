from sqlalchemy import create_engine

import json

with open('credentials.json') as f:
  credentials = json.load(f)

end_point = 'alex-aicore.c36j3dhgfor3.eu-west-2.rds.amazonaws.com'
port = '5432'
db_identifier = 'postgres'
engine = create_engine(f'postgresql://postgres:{credentials["password"]}@{end_point}/{db_identifier}').connect()

# from sqlalchemy.sql import text
#
# with engine.connect() as con:
#   file = open("query.sql")
#   query = text(file.read())
#
#   con.execute(query)


league_table.to_sql(con=database_connection, name="LEAGUE_TABLE", if_exists='replace',chunksize=100, index=False)