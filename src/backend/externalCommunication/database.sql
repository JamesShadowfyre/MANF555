Create Table IF NOT EXISTS user (
    id integer PRIMARY KEY autoincrement,
    username TEXT UNIQUE NOT NULL,
    password NOT NULL
)
