
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

session = get_session()
create_customer(session)
