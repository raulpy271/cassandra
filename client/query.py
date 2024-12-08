
from session import get_session


def show_customers(session):
    customers = session.execute("SELECT * FROM customer").all()
    print('--- Usuários do sistema ---')
    for customer in customers:
        print('Customer', customer.id, customer.username, customer.email, customer.gender)
    print(f'--- Total {len(customers)} ---')

def show_orders(session):
    orders = session.execute("SELECT * FROM orders").all()
    print('--- Pedidos do sistema ---')
    for order in orders:
        customer = session.execute(
            session.prepare("SELECT username FROM customer WHERE id = ? ALLOW FILTERING"),
            [order.customer]
        ).one()
        print('Pedido', order.id, order.paid, order.shipping_address, 'usuário do pedido', customer.username, len(order.products))
    print(f'--- Total {len(orders)} ---')

session = get_session()
show_orders(session)
