import requests
import json


class FPL_Engine:
    def __init__(self, credentials):
        self.credentials = credentials

    def get_fixtures():
        url = credentials["fixtures_url"]
        r = requests.get(url)
        json = r.json()
        return json

    def get_teams():
        url = credentials["teams_url"]
        r = requests.get(url)
        json = r.json()
        teams = json['teams']
        return teams

    def get_players():
        url = credentials["players_url"]
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

    def manager_fpl_data():
        url = credentials["login_url"]
        pwd = credentials["password"]
        email = credentials["email"]
        redirect_uri = credentials["redirect_uri"]
        app_name = credentials["app_name"]
        payload = {
            'password': pwd,
            'login': email,
            'redirect_uri': redirect_uri,
            'app': app_name
        }
        session = requests.session()
        session.post(url, data=payload)
        response = session.get(f'https://fantasy.premierleague.com/api/my-team/{alex_manager_id}/')
        json = response.json()
        return json


