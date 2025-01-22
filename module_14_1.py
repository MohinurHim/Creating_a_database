import sqlite3

# Задача "Первые пользователи":

connection = sqlite3.connect('not_telegram.db') # подключение к базе данных
cursor = connection.cursor() # объект курсор

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id  INTEGER PRIMARY KEY, 
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''') # создание таблицы Users

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# Заполнение 10 записями:
for i in range(10):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)", (f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

# Обновление balance у каждой 2ой записи начиная с 1ой на 500:
cursor.execute("UPDATE Users SET balance = ? WHERE id%2 <> ?", (500, 0))

# Удаление каждой 3 записи в таблице начиная с 1ой
cursor.execute("DELETE FROM Users WHERE (id+2)%3 = ?", (0,))

# Выборка всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age <> ?", (60,))
result = cursor.fetchall()
for res in result:
    print(f"Имя: {res[0]}| Почта: {res[1]} | Возраст: {res[2]} | Баланс: {res[3]}")
connection.commit()
connection.close()