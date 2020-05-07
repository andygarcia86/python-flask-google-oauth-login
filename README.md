# Python Flask Google oauth login

Sample demo for login in Python flask application using a google account

## Requirements

1. Python 3.4+

## Setup

### Setup Google Account

1. Open a browser and navigate to `https://console.developers.google.com/apis/credentials?pli=1`
2. Create a new Id for `OAuth 2.0 Client IDs`
3. Select `Web application`
4. Fill the field `Authorized JavaScript origins` with `https://127.0.0.1:5001`
5. Fill the field `Authorized redirect URIs` with `https://127.0.0.1:5001/login/callback`
6. Copy and update in the variables in the `app.py` file with the `Client ID` and the `Client secret` values.

### Run local Python FLask App

1. Open CMD or terminal with Administrator privileges
2. Move to the root folder of the project
3. Run `pip install -r requirements.txt` (Only the first time)
4. Run `python app.py` in the CMD
5. Open browser and navigate to `https://127.0.0.1:5001`

## Notes

Remove the website associated to the google account:

1. Navigate to `https://myaccount.google.com/permissions?gar=1`.
2. Search your application in the list.
3. Click in the `Remove Access` button.

## References Post

1. [Real Python - Flask google login](https://realpython.com/flask-google-login/)
2. [Serving HTML files with Flask](https://pythonise.com/series/learning-flask/rendering-html-files-with-flask)