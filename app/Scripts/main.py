import pandas as pd 
import pandas_datareader.data as pdr
import yfinance

yfinance.pdr_override()


data_inicial = "2024-01-01"
data_final = "2024-03-31"

tb_cotacao = pdr.get_data_yahoo("VILG11.SA", data_inicial, data_final)
print(tb_cotacao)
