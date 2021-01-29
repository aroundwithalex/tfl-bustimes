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


def read_with_names(url=DB_URI):
    with psql.connect(url) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'arrivals'"
        )
        names = cur.fetchall()
        cur.execute("SELECT * FROM arrivals")
        data = cur.fetchall()
        named_data = []
        for item in data:
            fresh_data = {
                a: b for a, b in zip(("".join(x) for x in names), (x for x in item))
            }
            named_data.append(fresh_data)
        return named_data
