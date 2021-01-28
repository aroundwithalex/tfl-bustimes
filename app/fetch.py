import requests

URL = 'https://api.tfl.gov.uk/StopPoint/490009333W/arrivals'

def fetch_data(url=URL):
    res = requests.get(url)
    return res.json()
