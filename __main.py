import json

from project.engine.data_engine import FPL_Engine

with open('credentials.json') as f:
  credentials = json.load(f)

engine = FPL_Engine(credentials)

engine.display_team()



import project.engine.data_engine
from importlib import reload

reload(project.engine.data_engine)


