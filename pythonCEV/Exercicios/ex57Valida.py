"""Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto."""
sexo = input("Digite seu sexo(M/F)")
while sexo.lower() not in ("mf") or len(sexo) != 1 or sexo == None:
    sexo = input("só M(masculino) ou F(feminino), digite novamente: ")
# essa validação é um pouco mais simples do que as que eu costumo fazer, como no exercício anterior
# onde uso o tratamento de excessão sem necessidade, mais uma lição do curso
if sexo.lower() == "f":
    sexo = "feminino"
else:
    sexo = "masculino"
print("Seu sexo é {}".format(sexo))
