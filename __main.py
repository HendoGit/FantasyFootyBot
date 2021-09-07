import json

from project.engine.data_engine import FPL_Engine

with open('credentials.json') as f:
  credentials = json.load(f)

engine = FPL_Engine(credentials)

teams = engine.get_teams()

print(teams)