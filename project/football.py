import requests
import json
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

def get_my_team(manager_id):
    url = f'https://fantasy.premierleague.com/api/my-team/{manager_id}/'
    r = requests.get(url)
    json = r.json()

    return json

alex_manager_id = '4186534'



fixtures = get_fixtures()
teams = get_teams()
players = get_players()

player_history, player_fixtures = get_detailed_player_info(5)

my_team = get_my_team(alex_manager_id)

names = [i['name'] for i in teams]

session = requests.session()

def get_pwd():

    with open('credentials.json') as f:
      credentials = json.load(f)


    return credentials["fantasy_pwd"]

def log_in():
    url = 'https://users.premierleague.com/accounts/login/'
    pwd = get_pwd()
    payload = {
     'password': pwd,
     'login': 'alexhenderson270@hotmail.com',
     'redirect_uri': 'https://fantasy.premierleague.com/a/login',
     'app': 'plfpl-web'
    }
    session = requests.session()
    session.post(url, data=payload)
    response = session.get(f'https://fantasy.premierleague.com/api/my-team/{alex_manager_id}/')
    json = response.json()

    return json


my_team=log_in()

