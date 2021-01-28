import requests
from datetime import datetime

URL = "https://api.tfl.gov.uk/StopPoint/490009333W/arrivals"


def fetch_data(url=URL):
    """
    Fetches data from TFL API

    Args:
        url: URL of TFL API

    Returns:
        None if no data or empty list returned
        Generator of data fetched from API

    Raises:
        ConnectionError: If unable to establish connection
    """
    res = requests.get(url)
    if res.ok:
        data = res.json()
        if not data:
            return None
        for bus in data:
            yield (bus)
    else:
        raise ConnectionError("Cannot connect to API")


def data_for_display(dct):
    """
    Filters and fixes data for display in Flask

    Args:
        dct: Dictionary of values returned from API request

    Returns:
        Filtered dictionary for display

    Raises:
        None
    """
    KEYS = [
        "vehicleId",
        "stationName",
        "lineName",
        "direction",
        "destinationName",
        "timeToStation",
        "towards",
        "expectedArrival",
    ]
    data = {a: b for a, b in dct.items() if a in KEYS}
    data["vehicleId"] = " ".join((data["vehicleId"][:4], data["vehicleId"][4:]))
    data["expectedArrival"] = " ".join(data["expectedArrival"].split("T")).strip("Z")
    return data
