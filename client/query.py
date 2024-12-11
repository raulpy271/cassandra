
from sys import argv

from session import get_session


def show_customers(session):
    customers = session.execute("SELECT * FROM customer").all()
    print('--- Usuários do sistema ---')
    for customer in customers:
        print('Customer', customer.id, customer.username, customer.email, customer.gender)
    print(f'--- Total {len(customers)} ---')

def show_products(session):
    products = session.execute("SELECT * FROM product").all()
    print('--- Produtos do sistema ---')
    for product in products:
        print('Product', product.id, product.name, product.base_price)
    print(f'--- Total {len(products)} ---')

def show_orders(session):
    orders = session.execute("SELECT * FROM orders").all()
    print('--- Pedidos do sistema ---')
    for order in orders:
        customer = session.execute(
            session.prepare("SELECT username FROM customer WHERE id = ?"),
            [order.customer]
        ).one()
        print('Pedido', order.id, order.paid, order.shipping_address, 'usuário do pedido', customer.username, len(order.products))
    print(f'--- Total {len(orders)} ---')

if __name__ == '__main__':
    session = get_session()
    queries = {
        'customer': show_customers,
        'product': show_products,
        'orders': show_orders,
    }
    if len(argv) > 1 and argv[1] in queries:
        queries[argv[1]](session)
    else:
        for query in queries.values():
            query(session)

