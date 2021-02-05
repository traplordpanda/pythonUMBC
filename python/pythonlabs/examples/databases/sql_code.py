#!/usr/bin/env python3
import sqlite3

connection = sqlite3.connect('dbase2.sqlite3')
print("connected to database")
cursor = connection.cursor()
sql_cmd = 'create table if not exists people ' + \
          '(name TEXT, job TEXT, pay INTEGER)'
cursor.execute(sql_cmd)

prompt = "Enter: <name> <job> <pay> (Or <enter> when done)"
sql_cmd = 'insert into people values(?,?,?)'
while True:
    line = input(prompt)
    if not line:
        break
    cursor.execute(sql_cmd, line.split())

rows = [['mike', 'dev', '50000'], ['joan', 'mus', '70000'],
        ['mike', 'adm', '40000'], ['peter', 'adm', '40000'],
        ['larry', 'dev', '55000'], ['moe', 'mus', '60000'],
        ['curley', 'adm', '45000']]

cursor.executemany(sql_cmd, rows)
connection.commit()

cursor.execute('select * from people')
for name, job, pay in cursor.fetchall():
    print(name, job, pay)
print("*" * 30)
cursor.execute('select name, pay from people where job = ?',
               ["adm"])
for name, pay in cursor.fetchall():
    print(name, pay)

cursor.close()
connection.close()
