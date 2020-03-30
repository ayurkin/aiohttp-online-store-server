venv:  ## create python env
	virtualenv -p ~/.pyenv/versions/3.7.4/bin/python venv

install:  ## install requirements
	venv/bin/pip install -r requirements.txt

run_server:  ## run server with  mongo in docker
	docker-compose up -d
	venv/bin/python -m app.main

mongo_stop: ## stop mongodb container
	docker-compose stop
