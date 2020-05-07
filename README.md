# Python Flask Google oauth login

Sample demo for login in Python flask application using a google account

## Requirements

1. Python 3.4+
2. Docker
3. My SQL

## Setup

1. Open a browser and navigate to `https://console.developers.google.com/apis/credentials?pli=1`
2. Create a new Id in `OAuth 2.0 Client IDs`
3. Copy and update in the env file the `Client ID` and the `Client secret`
4. Open CMD with Administrator privileges
5. Move to the root folder of the project
6. Run `pip install -r requirements.txt` (Only the first time)
7. Run `python app.py` in the CMD
8. Open browser and navigate to `https://127.0.0.1:5000`

## Setup Using Docker

- Debugging: `docker-compose -f docker-compose.yml -f docker-compose-debug-py.yml up --build`
- Development: `docker-compose -f docker-compose.yml up --build`

1. Open terminal or CMD console
2. Move to `flask` folder running `cd flask` command
3. Run `docker build -t flask-login-google:latest .`
4. Run `docker run -d -p 5000:5000 flask-login-google`
5. Open browser and navigate to `http://127.0.0.1:5000`

## References

1. [Real Python - Flask google login](https://realpython.com/flask-google-login/)
2. [Docker Flask Application](https://runnable.com/docker/python/dockerize-your-flask-application)
3. [Serving HTML files with Flask](https://pythonise.com/series/learning-flask/rendering-html-files-with-flask)