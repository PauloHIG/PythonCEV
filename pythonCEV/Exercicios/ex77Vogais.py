"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""
palavras = "Paulo", "ABACATE", "PEIXE", "TUPLA", "ALFABETO", "PYTHON"

for palavra in palavras:
    print(f"A palavra {palavra} tem as vogais:", end=" ")
    for letra in palavra:
        print(letra if letra.lower() in "aeiou" else "", end="")
    print("")

print("\nPalavras ao contrario só de brincadeira\n")
for palavra in palavras:
    print(palavra[::-1])
