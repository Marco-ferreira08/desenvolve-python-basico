genero = input ("Qual o seu gênro? Digite 'M' para 'masculino' e 'F' para 'feminino': ")
idade = int(input("Digite sua idade: "))
t_servico = int(input(" Digite seu tempo de serviço em anos: "))
aposentadoria = bool(False)

# Processamento: São testadas diferentes condições para a aposentadoria 
# em relação aos dados obtidos:

a = (genero == "F" and idade > 60) or (genero == "M" and idade > 65)
b = (t_servico >= 30)
c = (idade == 60 and t_servico >= 25)
aposentadoria = a or b or c

# Saída de Dados: Possibilidade da pessoa aposentar ou não de acordo com 
# os dados coletados
print(f"Aptidão para aposentar: {aposentadoria}")