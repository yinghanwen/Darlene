import sqlite3

connect = sqlite3.connect(".../data.db")
cur = connect.cursor()

sql_text = '''CREATE TABLE DATA
gid NUMBER,
uid NUMBER,
coins NUMBER,
state NUMBER
'''

