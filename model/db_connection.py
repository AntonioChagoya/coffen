import psycopg2


class DBConnection():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                "dbname='coffen' user='antonio' host='localhost' password='Arturo123.' port='5432'")
        except psycopg2.DatabaseError as err:
            print("Error: ", err)

    def write(self, data):
        if self.conn is not None:
            with self.conn.cursor() as cur:
                cur.execute("INSERT INTO users (name, password) VALUES (%(name)s, %(password)s)",
                            data)
                self.conn.commit()

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
