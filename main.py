import pandas as pd

from twilio.rest import Client

account_sid = "AC0280869aeb9f187753f6c7b54f4f5234"
auth_token = "3fc2d77bc4ffbd9c6940abe687f4831c"
client = Client(account_sid, auth_token)



list_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in list_meses:
    tab_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tab_vendas["Vendas"] > 55000).any():
        vendedor = tab_vendas.loc[tab_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tab_vendas.loc[tab_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        message = client.messages.create(
            to="+5599981189635",
            from_="+19036648107",
            body=f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}. Nand aqui cuzao")
        print(message.sid)


#fiz esse código com base no intensivo de python da Hashtag do YT.