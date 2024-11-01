frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
nomes = 'vinicius, jamilton, haviny, larissa, dinis'
print(nomes.split())
print(nomes.split(','))
hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))
# Como conectar(combinar) strings
hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))
