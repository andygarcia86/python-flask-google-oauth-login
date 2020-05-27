import os
from requests_oauthlib import OAuth2Session
from flask import Flask, request


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

oauth_providers = {
    "github": {
        "api_url": "https://api.github.com/user",
        "client_id": "",
        "client_secret": "",
        "scope": ["user"],
        "redirect_uri": "http://localhost:5000/oauth_callback?provider=github",
        "token_url": "https://github.com/login/oauth/access_token",
        "authorize_url": "https://github.com/login/oauth/authorize",
        "info_fn": lambda response: response.json()["login"]
    },
    "google": {
        "api_url": "https://www.googleapis.com/oauth2/v1/userinfo?alt=json",
        "client_id": "",
        "client_secret": "",
        "scope": ["https://www.googleapis.com/auth/userinfo.profile"],
        "redirect_uri": "http://localhost:5000/oauth_callback?provider=google",
        "token_url": "https://accounts.google.com/o/oauth2/token",
        "authorize_url": "https://accounts.google.com/o/oauth2/auth",
        "info_fn": lambda response: response.json()["name"]
    },
}

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def home():
    buttons_html = ""

    for key in oauth_providers.keys():
        oauth_provider_name = key
        oauth_provider = oauth_providers[oauth_provider_name]

        oauth = OAuth2Session(
            oauth_provider["client_id"],
            redirect_uri=oauth_provider['redirect_uri'],
            scope=oauth_provider["scope"],
        )

        login_url, state = oauth.authorization_url(
            oauth_provider["authorize_url"]
        )

        buttons_html = (
            f"{buttons_html}<br>"
            f'<br><a href="{login_url}">Login with {oauth_provider_name}</a>'
        )

    return buttons_html


@app.route("/oauth_callback")
def oauth_callback():
    oauth_provider_name = request.args.get("provider")

    oauth_provider = oauth_providers[oauth_provider_name]

    state = request.args.get("state")
    code = request.args.get("code")

    provider = OAuth2Session(
        oauth_provider["client_id"],
        redirect_uri=oauth_provider["redirect_uri"],
        state=state,
        scope=oauth_provider["scope"],
    )

    token = provider.fetch_token(
        oauth_provider["token_url"],
        client_secret=oauth_provider["client_secret"],
        code=code,
        authorization_response=request.url
        if oauth_provider_name == "github"
        else oauth_provider["redirect_uri"],
    )

    token_type = token["token_type"]
    access_token = token["access_token"]

    return (
        f'<a href="/profile?access_token={access_token}'
        f'&token_type={token_type}&provider={oauth_provider_name}">Profile</a>'
    )


@app.route("/profile")
def profile():
    oauth_provider_name = request.args.get("provider")

    oauth_provider = oauth_providers[oauth_provider_name]

    access_token = request.args.get("access_token")
    token_type = request.args.get("token_type")

    provider = OAuth2Session(
        oauth_provider["client_id"],
        token={
            "token_type": token_type,
            "access_token": access_token,
            "scope": oauth_provider["scope"],
        },
    )

    response = provider.get(oauth_provider["api_url"])

    return f'Profile: {oauth_provider["info_fn"](response)}'


if __name__ == "__main__": 
    app.run()
