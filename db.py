from app import DB_URI
import psycopg2 as psql
from datetime import datetime


def write_data(data, url=DB_URI):
    """
    Writes data to Postgres database

    Args:
        data: Data to be written to database
        url: URL of remotely hosted databases

    Raises:
        None

    """
    with psql.connect(url) as conn:
        cur = conn.cursor()
        for item in data:
            cur.execute(
                """INSERT INTO arrivals
                        (vehicle_reg, 
                            departing_station,
                            destination,
                            on_line,
                            expected_arrival,
                            data_collected
                            )
                            VALUES (
                            %(vehicleId)s,
                            %(stationName)s,
                            %(destinationName)s,
                            %(lineName)s,
                            %(expectedArrival)s,
                            %(data_collected)s);""",
                (item),
            )
        conn.commit()
        cur.close()


def read_data(url=DB_URI):
    with psql.connect(url) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM arrivals;")
        return cur.fetchall()
