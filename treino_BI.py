import pandas as pd
import numpy as np

df = pd.read_csv("datas/sql.csv")

print(df.columns)
print(df)
#print(df.isna().sum())
#NÃO EXISTE VALORES NULOS

#print(np.isinf(df["preco_unitario"].sum()))
#NENHUM VALOR INF

#print(df[["desconto", "preco_unitario", "quantidade"]])


df["Total_Venda"] = df["preco_unitario"] *  df["quantidade"]



print(df["Total_Venda"])

df["Total_Liquido"] = df["Total_Venda"] * (1 - df["desconto"])

print(df["Total_Liquido"])

total_vendedor = df.groupby("vendedor")["Total_Liquido"].sum().reset_index()


df["Categoria_Vendedor"] = np.where(
df["Total_Liquido"] < 5000, "Bronze",
np.where(df["Total_Liquido"] <= 10000, "Prata", "Ouro")

)


print(df[["vendedor","Categoria_Vendedor"]])


print(df.groupby(by=["vendedor", "Categoria_Vendedor"])["Total_Liquido"].sum())



print(df.groupby(by="vendedor")["Total_Liquido"].mean())

print(df.groupby(by="vendedor")["Total_Liquido"].sum())


df.to_csv("datas/sql.csv", index=False)

df.to_excel("vendas.xlsx", index=False)