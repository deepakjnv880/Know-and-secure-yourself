import sqlite3

DATABASE = "database1.db"
print("hi deepak i am in connection.py\n")
def create():

    COMMAND = """ create table users(
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    email TEXT NOT NULL,
    uname TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL
    );
    """

    conn = sqlite3.connect(DATABASE)
    curs = conn.cursor()
    curs.execute(COMMAND)
    conn.close()

def get_db():

    try:
        open(DATABASE)
        print("database is already created\n")

    except:
        create()
        print("Created the Database")

    return

if __name__ == '__main__':
    get_db()
