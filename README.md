# IMDB-FASTAPI

# Project requirement
- MongoDB Connection url

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

```shell
 docker build . -t imdb-test
```
- run docker container
```shell
 docker run -d -p 8080:80 imdb-test
 OR
 docker run -d -p 8000:80 imdb-test
```

