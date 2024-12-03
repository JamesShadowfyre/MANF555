Create Table IF NOT EXISTS user (
    id integer PRIMARY KEY autoincrement,
    username TEXT UNIQUE NOT NULL,
    password NOT NULL
);

Create Table IF NOT EXISTS workOrder (
    id integer PRIMARY KEY autoincrement
    clientid integer
    createdBy integer
    operatorid integer
    duration decimal
    quantity decimal
);


