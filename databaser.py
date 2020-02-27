import sqlite3

conn = sqlite3.connect('usuarios.db')

cursor = conn.cursor()

cursor.execute("""
create table if not exists usuarios(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username varchar (80) not null ,
    name varchar (80) not null ,
    email varchar (80) not null ,
    password varchar (80) not null
);
""")

print("Conectado ao banco de dados")
