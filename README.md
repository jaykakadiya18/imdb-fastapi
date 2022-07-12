# IMDB-FASTAPI

# Project requirement
- MongoDB Connection url

[x] does it
[] all test complete

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
- Access [docs](http://127.0.0.1:8000/docs)
