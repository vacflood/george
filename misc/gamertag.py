import requests

class Gamertag():
    def __init__(self) -> None:
        pass

    @staticmethod
    def check(gamertag: str) -> dict:
        url = f"https://gamertag.world/api/check?tag={gamertag}"
        payload = {}
        headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'content-type': 'application/json',
        'accept': '*/*',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if 'is available with an ID!' in response.json()['message']:
            return False
        else:
            return True