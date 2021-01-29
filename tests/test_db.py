import unittest
import psycopg2 as psql


def get_db_url(doc=".flaskenv"):
    with open(doc) as flaskenv:
        data = flaskenv.read()
        url = data.split("DATABASE_URL= ")[1]
        return url.strip()


class TestDB(unittest.TestCase):
    def test_conn(self):
        db_url = get_db_url()
        conn = psql.connect(db_url)

    def test_write(self):
        db_url = get_db_url()
        conn = psql.connect(db_url)
        cur = conn.cursor()
        try:
            cur.execute(
                """INSERT INTO arrivals 
                        (vehicle_reg,
                            departing_station,
                            destination,
                            on_line,
                            expected_arrival,
                            data_collected)
                        VALUES(%s, %s, %s,
                                %s, %s, %s);""",
                (
                    "YX19 RYR",
                    "Somewhere",
                    "Someplace",
                    "K1",
                    "2021-02-03 00:00:00",
                    "2021-01-01 00:00:00",
                ),
            )
            cur.close()
            conn.close()
        except Exception as exception:
            self.fail("Database write failed")

    def test_read(self):
        db_url = get_db_url()
        with psql.connect(db_url) as conn:
            cur = conn.cursor()
            cur.execute("""SELECT * FROM arrivals;""")
            data = cur.fetchall()
            print(data)
            self.assertIsInstance(data, list)
