"""
Provide information from the presidents table in the PostGRES database.
"""
import psycopg2, psycopg2.extras

president_query = "select * from presidents where termnum = %s"
all_presidents_query = "select * from presidents"

pg_conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password='scripts',
)
pg_cursor = pg_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def fetch_president(term_id):
    pg_cursor.execute(president_query, [term_id])
    row = pg_cursor.fetchone()
    if row:
        _convert_dates(row)
    else:
        row = {"status": "not found"}
    return row

def fetch_all_presidents():
    pg_cursor.execute(all_presidents_query)
    rows = pg_cursor.fetchall()
    for row in rows:
        _convert_dates(row)
    return rows

def _convert_dates(row):
    print(f"{row = }")

    for key in 'birthdate', 'deathdate', 'termstart', 'termend':
        # convert date to string because json can't parse date objects
        row[key] = str(row[key])
