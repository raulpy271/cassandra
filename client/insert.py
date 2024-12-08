
import os
import random
from datetime import date
from uuid import uuid4

from session import get_session

def create_customer(session):
    stmt = session.prepare("""
        insert into customer
            (username, id, fullname, email, phone, gender, birth_date, created, password_hash, password_salt)
            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """)
    nome = random.choice(['raul', 'eladio', 'catarina', 'debinha', 'dondoca', 'bené'])
    session.execute(stmt, [
        nome,
        uuid4(),
        nome,
        f'{nome}@ggg',
        '880999',
        random.choice(['male', 'female']),
        date(year=random.randint(1990, 2010), month=1, day=1),
        date.today(),
        str(random.randbytes(10)),
        str(random.randbytes(20)),
    ])

def create_product(session):
    stmt = session.prepare("""
        insert into product (id, base_price, name, description, available)
            values (?, ?, ?, ?, ?)
    """)
    product_id = uuid4()
    name = random.choice(['laptop', 'car', 'bike', 'motorcicle'])
    session.execute(stmt, [
        product_id,
        random.random() * 1000,
        name,
        name + ' is a good product, trust me!',
        random.randint(10, 100)
    ])
    stmt = session.prepare("""
        insert into product_image (id, product_id, altname, sizebin, resolution, format, data)
            values (?, ?, ?, ?, ?, ?, ?)
    """)
    image = random.choice(['im01.jpeg', 'im02.jpeg', 'im03.jpeg'])
    path = f'imgs/{image}'
    with open(path, 'rb') as imfile:
        session.execute(stmt, [
            uuid4(),
            product_id,
            name + ' ' + image,
            os.path.getsize(path),
            (1000, 1000),
            'jpeg',
            imfile.read()
        ])

def create_order(session):
    customer_id = random.choice(session.execute('select id from customer').all()).id
    products = random.choices(session.execute('select id, base_price from product').all(), k=random.randint(1, 5))
    products_ids = [p.id for p in products]
    price = sum(map(lambda p: p.base_price, products))
    addr = "Rua X Y, Xique-Xique BAHIA"
    stmt = session.prepare("""
        insert into orders (id, total_price, paid, customer, products, shipping_address, billing_address)
            values (?, ?, ?, ?, ?, ?, ?)
    """)
    session.execute(stmt, [
        uuid4(),
        price,
        random.random() > 0.5,
        customer_id,
        products_ids,
        addr,
        addr,
    ])

session = get_session()
create_order(session)

