# Создайте таблицу в БД, заполните минимум 10-ю записями. Половину записей удалите (DELETE), а вторую измените
# (с помощью UPDATE). Точное количество записей вы не знаете, поэтому код должен быть универсальным - для любого
# количества записей в таблице.

import sqlite3
conn = sqlite3.connect('new_db.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT, col_3 FLOAT) ''')
# cursor.execute(''' INSERT INTO table1(col_1, col_2, col_3) VALUES ('аpple',"kilogram",5.16) ''')
conn.commit()
cursor.execute('''UPDATE table1 SET col_1='jam', col_2='gram', col_3=12.21 WHERE id=?''', (10,))
conn.commit()
cursor.execute('''SELECT * FROM table1''')
k = cursor.fetchall()
for i in k:
    print(*i)

cursor.execute('''DELETE FROM table1 WHERE id%2=0''')
cursor.execute('''UPDATE table1 SET col_3='None' WHERE id%2!=0''')
cursor.execute('''SELECT * FROM table1''')
k = cursor.fetchall()
for i in k:
    print(*i)
conn.close()