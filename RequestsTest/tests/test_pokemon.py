import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'Your_Trainer_Token'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '1Your_Trainer_ID'

def test_check_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_check_trainer_name_in_response():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.json()['data'][0]['trainer_name'] == 'MrTest'