import sqlite3
import sqlite3 as sq


async def create_db():
    global db, cursor

    db = sq.connect("test.db")
    cursor = db.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS models(
        id INTEGER primary key AUTOINCREMENT,
        name TEXT,
        description TEXT,
        photo_id TEXT,
        link_file TEXT

        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS objects(
        id INTEGER primary key AUTOINCREMENT,
        name TEXT,
        description TEXT,
        photo_id TEXT,
        link_file TEXT

        )"""
    )
    db.commit()


async def add_data_model(name, description, photo_id, link_file):
    cursor.execute(
        """INSERT INTO models(name, description, photo_id, link_file)
         VALUES(?, ?, ?, ?)""", (
            name,
            description,
            photo_id,
            link_file,
        )
    )
    db.commit()


async def select_all_models():
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute(""" SELECT * FROM models """)
    response = cur.fetchall()
    return response


async def select_model_db(unique_id):
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute(f""" SELECT * FROM models WHERE id=?""", (unique_id,))
    response = cur.fetchone()
    return response


async def delete_model_db(unique_id, name):
    cursor.execute(f""" DELETE FROM models WHERE id={unique_id}""")
    db.commit()
    return f'Success delete model with name {name}'


async def update_name_model_db(unique_id, new_name):
    cursor.execute(f""" UPDATE models SET name='{new_name}' WHERE id={unique_id}""")
    db.commit()
    return f'Success update name model'


async def add_data_object(name, description, photo_id, link_file):
    cursor.execute(
        """INSERT INTO objects(name, description, photo_id, link_file)
         VALUES(?, ?, ?, ?)""", (
            name,
            description,
            photo_id,
            link_file,
        )
    )
    db.commit()
