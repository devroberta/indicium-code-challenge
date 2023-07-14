import psycopg
import pandas as pd
from datetime import datetime
import os

nameTable = input("Digite o nome da tabela a consultar: ")

conn = psycopg.connect(dbname="northwind", user="northwind_user", password="thewindisblowing", port="5432", host="localhost")
cur = conn.cursor()

try:
    query = f"select * from {nameTable}"
    df = pd.read_sql(query, conn)
    print(df)
except OSError:
    print('Tabela nao encontrada.')
    nameTable = ""

try:
    if nameTable != "":
        # criar diretorios
        pathFile = f'./data/postgres/{nameTable}/{datetime.now().date()}'
        os.makedirs(pathFile)

        # cria o nome do arquivo
        fileName = f'/{nameTable}.cvs'

        # grava o data frame em arquivo .csv
        df.to_csv(f'{pathFile}{fileName}')

except OSError:
    print('Arquivo nao pode ser gerado.')
