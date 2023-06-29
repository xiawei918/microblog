# microblog

A microblog created using Flask. See [demo](http://allendalemicroblog.com/).

## Start the service via flask local server

1. create a virtual environment using `Python`

   `python3 -m venv venv`
   
3. Activate the newly created virtual environment

   `source venv/bin/activate`
   
5. Install dependencies from `requirements.txt`
   
   `pip install -r requirements.txt`
   
7. Set Flask app environment variable

   `export FLASK_APP=microblog.py`
   
9. Start up flask local server

   `flask run`
   
11. Then navigate to http://localhost:5000 to view the app.

## Start the service via docker
1. Ensure [Docker](https://www.docker.com/) is installed.
2. Just run `docker-compose-up`
3. Then navigate to http://localhost:8000 to view the app.