from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('H:/Projects/flask_app/members.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite.db'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db