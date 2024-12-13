
from time import perf_counter

from session import get_session


QUERIES_COUNT = 100

def count_orders(session):
    username = 'raul' 
    customer = session.execute(
        session.prepare("SELECT id FROM customer WHERE username = ? ALLOW FILTERING"),
        [username]
    ).one()
    orders = session.execute(
        session.prepare("SELECT * FROM orders WHERE customer = ? ALLOW FILTERING"),
        [customer.id]
    ).all()
    return len(orders)

def query_images(session):
    product = session.execute("SELECT id FROM product").one()
    images = session.execute(
        session.prepare("SELECT * FROM product_image WHERE product_id = ? ALLOW FILTERING"),
        [product.id]
    ).all()
    for img in images:
        for col in img:
            continue

def query_one_customer(session):
    customer = session.execute("SELECT * FROM customer").one()
    for col in customer:
        continue

def calculate_time(operation):
    session = get_session()
    t1_start = perf_counter()
    for _ in range(QUERIES_COUNT):
        operation(session)
    t1_stop = perf_counter()
    time_elapsed = t1_stop - t1_start
    print(f"Tempo total ao executar {operation.__name__} {QUERIES_COUNT}x: {time_elapsed:.2f} (s)")

if __name__ == '__main__':
    calculate_time(query_one_customer)
    calculate_time(count_orders)
    calculate_time(query_images)

