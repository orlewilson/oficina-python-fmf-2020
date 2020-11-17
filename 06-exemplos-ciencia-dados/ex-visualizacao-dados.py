'''

	Oficinas da Semana - Python: Por Onde Começar e Quais Suas Aplicações?
	Facilitador:    Orlewilson Bentes Maia
	Data:           17/11/2020
	Nome:           Seu nome
    Descrição:      Pandas - leitura de arquivo .csv e visualização de dados

'''

# importação de bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# leitura de dados
df = pd.read_csv("airbnb-nyc-2019.csv", sep=";")

# manipulação dos dados lidos
print(df)

df2 = df[(df["price"] >= 0)]

print(df2.groupby("neighbourhood").mean()["price"].sort_values())

df2.groupby("neighbourhood").mean()["price"].sort_values().nlargest(5)


# visualização dos dados lidos
df2["price"].plot.hist()
plt.show() # mostrar janela

df2["price"].plot.hist(bins=30, edgecolor='black')
plt.show()


df2["neighbourhood"].value_counts().nlargest(5).plot.bar()
plt.show()

df2["neighbourhood"].value_counts().nlargest(5).plot.barh(title="Número de apartamentos")
plt.show()
