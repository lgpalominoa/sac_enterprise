import requests
from config.settings import USER_AGENT, HTTP_TIMEOUT

def geocode(query: str):
    r = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={
            "q": query,
            "countrycodes": "co",
            "format": "json",
            "limit": 1
        },
        headers={"User-Agent": USER_AGENT},
        timeout=HTTP_TIMEOUT
    )

    data = r.json()
    if not data:
        return None

    return float(data[0]["lat"]), float(data[0]["lon"])
