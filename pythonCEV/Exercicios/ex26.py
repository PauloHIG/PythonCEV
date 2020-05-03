#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: '))
frase = frase.strip()
print('A letra "a" aparece {} vezes'.format(frase.lower().count('a')))
print('A primeira letra "a" está na posição {}'.format(frase.lower().find('a')+1))
print('A ultima letra "a" do seu nome está na posição {}'.format(frase.lower().rfind('a')+1))