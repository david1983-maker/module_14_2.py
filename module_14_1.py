import sqlite3

with sqlite3.connect('not_telegram.db') as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
id integer PRIMARY KEY,
username text NOT NULL,
email text NOT NULL,
age integer,
balance integer NOT NULL
)""")
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
x = 1
for i in range(10, 110, 10):
    cursor.execute('INSERT INTO Users(username, email,age,balance)VALUES(?,?,?,?)',
                   (f'User{x}', f'example{x}@gmail.com', f'{i}', 1000))
    x += 1
for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id =?', (500, int(i)))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', int(i),))

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT * FROM Users WHERE age != ?', (60,))

# for i in cursor.fetchall():
#     print(f'Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}')

cursor.execute('SELECT COUNT(*) FROM Users ')
total = cursor.fetchone()
print(total)

cursor.execute('SELECT SUM(balance) FROM Users')
total_users = cursor.fetchone()
print(total_users)

cursor.execute('SELECT AVG(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(total_balance)

db.commit()
