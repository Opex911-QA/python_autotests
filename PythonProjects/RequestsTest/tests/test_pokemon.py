import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b556f05ef999c31e7b15671151f1c950'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '6077'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Opex911'

@pytest.mark.parametrize('key, value', [('trainer_name','Opex911'),('id', TRAINER_ID)])
def test_prmtrz(key, value):
    responce_prmtrz = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert responce_prmtrz.json()["data"][0][key] == value