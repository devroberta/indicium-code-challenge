import pandas as pd
from datetime import datetime


def checkFile():
    # receber caminho do arquivo
    pathFile = input("Informe o caminho e nome do arquivo: ")
    if pathFile == '':
        pathFile = "./data/order_details.csv"
    df = pd.read_csv(pathFile)
    print(df)
    # info da tabela importada do .csv
    print(df.info())
    # info resumida da tabela para ver valores nulos
    print(df.isna().sum())
    # gera novo arquivo csv analisando e extraindo apenas registros validos
    newPathFile = f"./data/order_details_{datetime.now().date()}.csv"
    df.to_csv(newPathFile)
    return newPathFile

checkFile()