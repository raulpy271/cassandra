
CREATE TABLE IF NOT EXISTS store.product (
    id uuid,
    base_price decimal,
    name text,
    description text,
    available int,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS store.orders (
    id uuid,
    total_price decimal,
    paid boolean,
    customer uuid,
    products list<uuid>,
    shipping_address text,
    billing_address text,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS store.customer (
    username text,
    id uuid,
    fullname text,
    email text,
    phone text,
    gender text,
    birth_date date,
    created date,
    password_hash text,
    password_salt text,
    PRIMARY KEY (username, id)
);

