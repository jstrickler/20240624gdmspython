import sys
import sqlite3
import logging

logging.basicConfig(
     level=logging.INFO,
)

conn = None

logging.info("starting program")

try:
    conn = sqlite3.connect('POTUS/presidents.db')
except sqlite3.DatabaseError as err:
    logging.exception(err)
    print("exiting...")
else:
    cursor = conn.cursor()
    #  execute SQL code here....
finally:  # cleanup clause
        if conn is not None:
            conn.close()

try:
    with sqlite3.connect('/oz/wombats.db') as conn:
        # blah blah
        cursor = conn.cursor()
except sqlite3.OperationalError as err:
    print(err)
    # log, etc here

logging.info("ending program")
