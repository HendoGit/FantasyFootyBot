from sqlalchemy import create_engine

import json

with open('credentials.json') as f:
  credentials = json.load(f)

end_point = 'alex-aicore.c36j3dhgfor3.eu-west-2.rds.amazonaws.com'
port = '5432'
db_identifier = 'alex-aicore'
engine = create_engine(f'postgresql://postgres:{credentials["password"]}@{end_point}:{port}/{db_identifier}')