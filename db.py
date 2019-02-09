import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Connection Successful.")
        c = conn.cursor()
        c.execute("CREATE TABLE bridges(\
            NAME varchar(128),\
            RARITY int,\
            EXPERIENCE int,\
            MATERIAL int,\
            TYPE int,\
            STRENGTH int,\
            LENGTH int,\
            WIDTH int,\
            HEIGHT int
            )")
    except Error as e:
        print(e)
    finally:
        conn.close()

def connect(db_file):
    try:
        return sqlite3.connect(db_file)
    except Error as e:
        print(e)

def add_bridge(conn, bridge):
    c = conn.cursor()
    c.execute("INSERT INTO bridges VALUES \
        '{bridge.name}',\
        '{bridge.rarity}',\
        '{bridge.experience}',\
        '{bridge.material}',\
        '{bridge.type}',\
        '{bridge.strength}',\
        '{bridge.length}',\
        '{bridge.width}',\
        '{bridge.height}")


if __name__ == '__main__':
    create_connection("/home/alex/Programs/Python/Bridge-Breeder/bridges.db")
