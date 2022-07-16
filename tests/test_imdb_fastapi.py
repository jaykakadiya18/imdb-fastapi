from fastapi.testclient import TestClient
from server.app import app

client = TestClient(app)

movie_data = {
    "popularity": 99,
    "director": "Cristopher nolan",
    "genre": [
      "thriller",
      "action"
    ],
    "imdb_score": 9.6,
    "name": "The dark knight"
}

login_data = {
    "email": "jaykakadiya2014@gmail.com",
    "password": "123456"
}

login_data_failed = {
    "email": "dummy@gmail.com",
    "password": "wrong_password"
}

def test_login():
    response = client.post("/accounts/login", json=login_data)
    assert response.status_code == 200

def test_login_failed():
    response = client.post("/accounts/login", json=login_data_failed)
    assert response.status_code == 404

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"knock knock!!!": "Who's there..."}

def test_create_movie():
    response = client.post("/accounts/login", json=login_data)
    assert response.status_code == 200
    resp = response.json()
    headers = {"Authorization": f"Bearer {resp['access_token']}"}
    response = client.post("/imdb/movies", json=movie_data, headers=headers)
    assert response.status_code == 200

def test_search():
    
    response = client.get("/imdb/movies?search=batman")
    assert response.status_code == 200
