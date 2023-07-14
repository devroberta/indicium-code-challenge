import psycopg
import pandas as pd

dateOrders = input("Digite a data a consultar ('yyyy-MM-dd'): ")

conn = psycopg.connect(dbname="northwind", user="northwind_user", password="thewindisblowing", port="5432", host="localhost")
cur = conn.cursor()

try:
    query = f"select distinct o.order_id, p.product_id, c.company_name, e.first_name, o.order_date, od.unit_price, od.quantity, od.discount from orders as o " \
            f"inner join order_details as od on od.order_id = o.order_id " \
            f"inner join products as p on p.product_id = od.product_id " \
            f"inner join customers as c on c.customer_id = o.customer_id " \
            f"inner join employees as e on e.employee_id = o.employee_id " \
            f"where o.order_date = '{dateOrders}'"

    df = pd.read_sql(query, conn)
    print(df.head())

except OSError:
    print('Erro acesso a consulta.')