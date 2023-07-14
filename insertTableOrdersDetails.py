import psycopg
import pandas as pd
import verifyFileCSV


pathFile = verifyFileCSV.checkFile()
tableName = 'order_details'

conn = psycopg.connect(dbname="northwind", user="northwind_user", password="thewindisblowing", port="5432", host="localhost")
cur = conn.cursor()

try:
    df = pd.read_csv(pathFile)
    print(df)
    for i, row in df.iterrows():
        line = [int(row[1]), int(row[2]), float(row[3]), int(row[4]), float(row[5])]
        print(line)
        sql = "INSERT INTO order_details (order_id, product_id, unit_price, quantity, discount) VALUES (%s,%s,%s,%s,%s)"
        cur.execute(sql, line)

    conn.commit()
    conn.close()

except OSError:
    print('Erro acesso a consulta.')

