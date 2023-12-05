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
    cursor.execute(""" SELECT * FROM models """)
    response = cursor.fetchall()

    return response


async def select_model_db(unique_id):
    cursor.execute(f""" SELECT * FROM models WHERE id=?""", (unique_id,))
    response = cursor.fetchall()
    return response


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
