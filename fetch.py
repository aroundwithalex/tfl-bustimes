import requests
from datetime import timedelta, datetime

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
        return data
    else:
        raise ConnectionError("Cannot connect to API")


def data_for_display(data):
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
    filtered_list = []
    for bus in data:
        new_bus = {a: b for a, b in bus.items() if a in KEYS}
        new_bus["vehicleId"] = " ".join((bus["vehicleId"][:4], bus["vehicleId"][4:]))
        new_bus["expectedArrival"] = " ".join(bus["expectedArrival"].split("T")).strip(
            "Z"
        )
        new_bus["timeToStation"] = str(timedelta(seconds=bus["timeToStation"]))
        new_bus["direction"] = bus["direction"].title()
        new_bus["data_collected"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filtered_list.append(new_bus)
    return tuple(filtered_list)
