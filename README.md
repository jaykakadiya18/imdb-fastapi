# IMDB-FASTAPI

## Project requirement
- MongoDB Connection url
---
## Heroku Links
- Access [docs](https://imdb-fastapi.herokuapp.com/docs)
- Access [redocs](https://imdb-fastapi.herokuapp.com/redoc)

---
## How to run in local env:
- git clone 
```shell
 https://github.com/jaykakadiya18/imdb-fastapi.git
```
- you can use requrenment.txt file OR you can use poetry as well pyproject.toml
```shell
 python3 -m pip install -r requirements.txt
```
run project
```shell
 python main.py
```
---
## ENDPOINTS
- root
```http
 https://imdb-fastapi.herokuapp.com/
```
- Signup (Admin)
- 1 username
- 2 email
- 3 password
```http
 https://imdb-fastapi.herokuapp.com/accounts/signup
```
- Login (Admin)
- 1 email
- 2 password
```http
 https://imdb-fastapi.herokuapp.com/accounts/login
```
- Add Movie (Admin)
- 1 popularity
- 2 director
- 3 genre
- 4 imdb_score
- 5 name
```http
 https://imdb-fastapi.herokuapp.com/imdb/movies/{id}
```
- Update Movie (Admin)
- 1 popularity
- 2 director
- 3 genre
- 4 imdb_score
- 5 name
```http
 https://imdb-fastapi.herokuapp.com/imdb/movies/{id}
```
- Delete Movie (Admin)
```http
 https://imdb-fastapi.herokuapp.com/imdb/movies/{id}
```
- Search Movie (Admin)
```http
 https://imdb-fastapi.herokuapp.com/imdb/movies/search
```
- Search Movie (User)
```http
 https://imdb-fastapi.herokuapp.com/imdb/movies/search
```

