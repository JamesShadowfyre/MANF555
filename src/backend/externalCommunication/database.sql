Create Table IF NOT EXISTS user (
    id integer PRIMARY KEY autoincrement,
    username TEXT UNIQUE NOT NULL,
    password NOT NULL,
    admin bool
);

Create Table IF NOT EXISTS workOrder (
    id integer PRIMARY KEY autoincrement,
    clientid integer,
    createdBy integer,
    operatorid integer,
    duration decimal,
    quantity decimal,
    FOREIGN KEY (clientid) REFERENCES customer(id),
    FOREIGN KEY (createdBy) REFERENCES user(id),
    FOREIGN KEY (operatorid) REFERENCES operator(id)
);

Create Table IF NOT EXISTS workOrderItemsList (
    workOrderid integer,
    itemid integer,
    quantity decimal,
    PRIMARY KEY (workOrderid, itemid),
    FOREIGN KEY (workOrderid) REFERENCES workOrder(id),
    FOREIGN KEY (itemid) REFERENCES item(id)
);

Create Table IF NOT EXISTS item (
    id integer PRIMARY KEY autoincrement,
    name TEXT,
    colour TEXT,
    averageCost decimal,
    machine TEXT,
    quantity decimal
);

Create Table IF NOT EXISTS operator (
    id integer PRIMARY KEY autoincrement,
    name TEXT,
    startTime integer,
    daylength decimal
);

Create Table IF NOT EXISTS customer (
    id integer PRIMARY KEY autoincrement,
    accountName TEXT,
    streetAddress1 TEXT,
    streetAddress2 TEXT,
    city TEXT,
    region TEXT,
    country TEXT,
    phoneNumber TEXT,
    email TEXT,
    billingstreetAddress1 TEXT,
    billingstreetAddress2 TEXT,
    billingcity TEXT,
    billingregion TEXT,
    billingcountry TEXT,
    billingphoneNumber TEXT,
    billingEmail TEXT
);
