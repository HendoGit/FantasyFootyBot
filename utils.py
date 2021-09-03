import requests
import pandas as pd
import numpy as np


def get_fixtures():
    url = 'https://fantasy.premierleague.com/api/fixtures/'
    r = requests.get(url)
    json = r.json()
    return json

def get_teams():
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    r = requests.get(url)
    json = r.json()
    teams = json['teams']
    return teams

def get_players():
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    r = requests.get(url)
    json = r.json()
    players = json['elements']
    return players

def get_detailed_player_info(player_id):
    url = f'https://fantasy.premierleague.com/api/element-summary/{player_id}/'
    r = requests.get(url)
    json = r.json()
    history = json['history']
    future = json['fixtures']
    return history, future


fixtures = get_fixtures()
teams = get_teams()
players = get_players()

player_history, player_fixtures = get_detailed_player_info(5)

