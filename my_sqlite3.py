# -*- coding: utf-8

import sqlite3

dbname = 'database.db'

conn = sqlite3.connect(dbname)
c = conn.cursor()

# executeメソッドでSQL文を実行する
create_table = '''create table users (id int, name varchar(64),
                  age int, gender varchar(32))'''
c.execute(create_table)

# SQL文に値をセットする場合は，Pythonのformatメソッドなどは使わずに，
# セットしたい場所に?を記述し，executeメソッドの第2引数に?に当てはめる値を
# タプルで渡す．
sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
user = (1, 'Taro', 20, 'male')
c.execute(sql, user)

# 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
# executemanyメソッドを実行する
insert_sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
users = [
    (2, 'Shota', 54, 'male'),
    (3, 'Nana', 40, 'female'),
    (4, 'Tooru', 78, 'male'),
    (5, 'Saki', 31, 'female')
]
c.executemany(insert_sql, users)
conn.commit()

select_sql = 'select * from users'
for row in c.execute(select_sql):
    print(row)

conn.close()
