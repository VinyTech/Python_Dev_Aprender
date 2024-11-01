teclado = 'teclado'
print(teclado[-1])
print(teclado.index('l'))
print(teclado[teclado.index('l')])
frase = 'Clean Code'
print(frase.rindex('C'))

# Desafio 1 => Encontre o índice de 'o' dentro da variável "bbiblioteca" 
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

# Desafio 2 => Usando a frase 'Desenvolvimento De Aplicações', imprima apenas "De Aplicações"
desafio = 'Desenvolvimento De Aplicações'
indice_d = desafio.rindex('D')
indice_s = desafio.rindex('s')
print(desafio[indice_d:indice_s+1])