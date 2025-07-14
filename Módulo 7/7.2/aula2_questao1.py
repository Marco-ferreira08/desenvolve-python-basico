mes_lista = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
               "Julho", "Agosto", "Setembro", "Outubro", "Novenbro", "Dezembro"] 

data = input("Digite a sua data de nscimento (dd/mm/aaaa): ")

dia = data[:2]
mes_texto = (data[3:5])
mes_numero = int(mes_texto[2]) if mes_texto[1] == "0" else int(mes_texto)
mes_extenso = mes_lista[(mes_numero - 1)]
ano = data[6:]

print(f"Você nasceu em {dia} de {mes_extenso} de {ano}")