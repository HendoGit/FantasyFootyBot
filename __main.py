import json

from project.scraper.data_engine import FPL_Engine

with open('credentials.json') as f:
  credentials = json.load(f)

engine = FPL_Engine(credentials)

fixtures = FPL_Engine.get_fixtures()

print(fixtures)