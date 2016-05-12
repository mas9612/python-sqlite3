# coding: utf-8

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

t = ('RHAT',)
c.execute('select * from stocks where symbol=?', t)
print(c.fetchone())

purchases = [
        ('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
        ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
        ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
        ]
c.executemany('insert into stocks values (?,?,?,?,?)', purchases)
conn.commit()

conn.close()
