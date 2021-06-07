import sqlite3
from sqlite3.dbapi2 import IntegrityError


connection = sqlite3.connect('database.db')

if __name__ == '__main__':
    with connection as conn:
        cur = conn.cursor()
        cur.executescript('''
            CREATE TABLE users (
                username TEXT unique, 
                fullname TEXT, 
                password TEXT
            );
            
            INSERT INTO users (username, fullname, password)
            VALUES (
                'demo_user',
                'Alpha',
                'password'
            );
        ''')


def insert(sql, params):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute(sql, params)


def select(sql, params):
    with connection as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql, params)
        results = [dict(row) for row in cur.fetchall()]

    return results


def user_exists(username, password=None):
    sql = "SELECT username, password FROM users WHERE username = ?"
    params = (username,)

    results = select(sql, params)

    if len(results):
        if password is None:
            return True

        return results[0]['password'] == password

    return None


def add_user(username, real_name, password):
    sql = "INSERT INTO users (username, fullname, password) VALUES (?,?,?)"
    query_params = (username, real_name, password)

    try:
        insert(sql, query_params)
        return True
    except IntegrityError:
        return False
