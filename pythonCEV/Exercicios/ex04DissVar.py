print("Dissecando uma variavel")
var = input("Digite algo: ")

print("O tipo primitivo da variavel é: ", type(var))
print("É um valor numérico?", var.isnumeric())
print("É alfanumérico?", var.isalnum())
print("É alpha(Alfabético)?", var.isalpha())
print("Só tem espaços?", var.isspace())
print("Só tem letras maiusculas?", var.isupper())
print("Só tem letras minusculas?", var.islower())
print("É printavel?", var.isprintable())
print("Está capitalizada?", var.istitle())  # mistura de maiuscula e minuscula
