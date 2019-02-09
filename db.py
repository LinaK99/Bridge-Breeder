import sqlite3
from sqlite3 import Error

from bridge import Bridge

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Connection Successful.")
        c = conn.cursor()
        c.execute("CREATE TABLE bridges(\
            name varchar(128),\
            rarity int,\
            experience int,\
            material int,\
            type int,\
            strength int,\
            length int,\
            width int,\
            height int\
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
    sql = "INSERT INTO bridges(name, rarity, experience,\
    material, type, strength, length, width, height) VALUES\
        ('" + bridge.name + "',"\
        + str(bridge.rarity) + ","\
        + str(bridge.experience) + ","\
        + str(bridge.material) + ","\
        + str(bridge.type) + ","\
        + str(bridge.strength) + ","\
        + str(bridge.length) + ","\
        + str(bridge.width) + ","\
        + str(bridge.height) + ")"
    c.execute(sql)
    conn.commit()
    print(sql)


if __name__ == '__main__':
    create_connection("/home/alex/Programs/Python/Bridge-Breeder/bridges.db")
