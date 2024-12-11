
CREATE KEYSPACE IF NOT EXISTS store
    WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };

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
    id uuid,
    username text,
    fullname text,
    email text,
    phone text,
    gender text,
    birth_date date,
    created date,
    password_hash text,
    password_salt text,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS store.product_image (
    id uuid,
    product_id uuid,
    altname text,
    sizebin int,
    resolution tuple<int, int>,
    format text,
    data blob, 
    PRIMARY KEY (id)
);

