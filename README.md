# Aiohttp REST server

Aiohttp online store server for Python 3.7.4 with mongodb in docker container. Inspired by https://github.com/sneawo/asyncio-rest-example

## Requirements:

-  Pyenv, python 3.7.4: https://khashtamov.com/ru/pyenv-python/

- docker: https://www.digitalocean.com/community/tutorials/docker-ubuntu-18-04-1-ru

- docker-compose: https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04-ru


## Usage:

Makefile commands:

1. **venv** — create python env
2. **install** — install requirements
3. **run_server** — run server with  mongo in docker
4. **mongo_stop** — stop mongodb container

Example: make venv

## Requests with curl:

### Create item

```shell
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Honor","description":"Mobile phone", "parameters":{"model":"p20 pro","color":"white","producer":"CN"}}' \
  http://localhost:8080/items
```

answer:

```json
{"description": "Mobile phone", "id": "5e81957f024b09b281d99efd", "parameters": {"model": "p20 pro", "color": "white", "producer": "CN"}, "name": "Honor"}
```

### Find item by id

```shell
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"id":"5e81957f024b09b281d99efd"}' \
  http://localhost:8080/items/find-by-id
```

answer:

```json
{"description": "Mobile phone", "id": "5e81957f024b09b281d99efd", "parameters": {"model": "p20 pro", "color": "white", "producer": "CN"}, "name": "Honor"}
```

### Filter item 

Answer is name of items

First we add second phone

```json
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Samsung","description":"Mobile phone", "parameters":{"model":"galaxy s20","color":"black","producer":"KR"}}' \
  http://localhost:8080/items
```

#### List all names

```shell
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{}' \
  http://localhost:8080/items/filter
```

answer

```
["Honor", "Samsung"]
```

#### By name

```shell
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Honor"}' \
  http://localhost:8080/items/filter
```

answer

```
["Honor"]
```

#### By parameter key/value

```shell
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"color":"white"}' \
  http://localhost:8080/items/filter
```

answer

```
["Honor"]
```

#### Filtering both by name and key/value

```shell
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Samsung","color":"black"}' \
  http://localhost:8080/items/filter
```

answer

```
["Samsung"]
```
