# # palindromos 
# #strip() remove os espaços em branco no inicio ou no fim da frase
frase = str(input('Digite uma frase: ')).strip().upper()
# # split() divide as palavras a cada espaço
palavras = frase.split()
# # join () juntas frases
junto = ''.join(palavras) 
inverso = ''
# # começa no len - 1 (do final) e vai ate antes do  inicio (-1) e vai do final pro inicio (-1)
for letra in range(len(junto) -1, -1, -1):
    inverso+=junto[letra]
print(junto,inverso)
if inverso == junto:
    print("A {} é palindromo".format(frase) )
else:
    print('A palavra "{}" não é palindromo e sua versão ao contrario é "{}"'.format(frase,inverso))


