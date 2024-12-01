import sqlite3


connection = sqlite3.connect("itstep_DB.sl3", 5) #ствоює файл таблиці
cur = connection.cursor()

print(connection)
print(cur)
#cur.execute("CREATE TABLE first_table (name TEXT);") створює таблицю
#cur.execute("INSERT INTO first_table (name) VALUES ('Nick');") додає ніка в таблицю
#cur.execute("INSERT INTO first_table (name) VALUES ('Alice');") додає алісу в таблицю
cur.execute("SELECT rowid, name FROM first_table;") #зчитує таблицю
#cur.execute("SELECT rowid, name FROM first_table WHERE rowid=2;") зчитує другу колонку
#cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=2") замінює алісу на катю
#cur.execute("DELETE FROM first_table WHERE rowid=1;") видаляє першу колонку в таблиці
#cur.execute("DROP TABLE first_table;") видаляэ всю таблицю

connection.commit() #додає до таблиці код зверху

res = cur.fetchall() #повертає відповідь з бази данних
print(res)
connection.close() #закриває таблицю
