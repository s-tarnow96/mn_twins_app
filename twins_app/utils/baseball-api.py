import requests
from ratelimit import limits, sleep_and_retry


ONE_HOUR = 3600
ONE_DAY = 86400


@sleep_and_retry
@limits(calls=100, period=ONE_DAY)
def get_leagues():
    url = "https://api-baseball.p.rapidapi.com/leagues"

    querystring = {"name": "mlb"}

    headers = {
        'x-rapidapi-key': "934ac43726msh4216b99e71e3c53p186cd8jsn9aae033ed353",
        'x-rapidapi-host': "api-baseball.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
