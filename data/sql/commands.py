import sqlite3
import sqlite3 as sq

DATABASE_NAME = "copy.db"


async def create_db():
    global db, cursor

    db = sq.connect(DATABASE_NAME)
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


async def add_data_model(name: str, description: str, photo_id: str, link_file: str):
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


async def select_model_db(unique_id: int):
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute(f""" SELECT * FROM models WHERE id=?""", (unique_id,))
    response = cur.fetchone()
    return response


async def delete_model_db(unique_id: int, name: str) -> str:
    cursor.execute(f""" DELETE FROM models WHERE id={unique_id}""")
    db.commit()
    return f'Success delete model with name {name}'


async def update_name_model_db(unique_id: int, new_name: str) -> str:
    cursor.execute(f""" UPDATE models SET name='{new_name}' WHERE id={unique_id}""")
    db.commit()
    return f'Success update name model'


async def update_description_model_db(unique_id: int, new_description: str) -> str:
    cursor.execute(f""" UPDATE models SET description='{new_description}' WHERE id={unique_id}""")
    db.commit()
    return f'Success update description model'


async def update_photo_model_db(unique_id: int, new_photo_id: str) -> str:
    cursor.execute(f""" UPDATE models SET photo_id='{new_photo_id}' WHERE id={unique_id}""")
    db.commit()
    return f'Success update photo model'


async def update_file_link_model_db(unique_id: int, new_file_link: str) -> str:
    cursor.execute(f""" UPDATE models SET link_file='{new_file_link}' WHERE id={unique_id}""")
    db.commit()
    return f'Success update link file model'


async def add_data_object(name: str, description: str, photo_id: str, link_file: str):
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


async def select_all_objects():
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute(""" SELECT * FROM objects """)
    response = cur.fetchall()
    return response


async def select_object_db(unique_id: int):
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute(f""" SELECT * FROM objects WHERE id=?""", (unique_id,))
    response = cur.fetchone()
    return response


async def delete_object_db(unique_id: int, name: str) -> str:
    cursor.execute(f""" DELETE FROM objects WHERE id={unique_id}""")
    db.commit()
    return f'Success delete object with name {name}'
