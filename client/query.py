
from session import get_session


def show_customers(session):
    customers = session.execute("SELECT * FROM customer").all()
    print('--- Usuários do sistema ---')
    for customer in customers:
        print('Customer', customer.id, customer.username, customer.email, customer.gender)
    print(f'--- Total {len(customers)} ---')

session = get_session()
show_customers(session)
