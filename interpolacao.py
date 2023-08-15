#INTERPOLAÇÂO DE STRINGS
# Estilo antigo de interpolação (Método não mais utilizado)
nome = "John"
idade = 28
profissao = "Data Analytics"
linguagem = "Python"

print("Oi, me chamo %s. Eu tenho %d anos de idade, trabalho como %s, e estou matriculado no curso de %s."% (nome, idade, profissao, linguagem))

#Legendas: 
# %s = tipo string
# %d = tipo inteiras




'''Estilo Format (Melhor que a anterior, porém apresenta o mesmo problema, onde as variáveis devem ser declarada e colocadas na messma ordem em que foram declaradas dentro da string, 
para que o valor seja devidamente tribuído a sua variável de destino'''

nome = "John"
idade = 27 
profissao = "Data Analytics"
linguagem = "Python"

print("Oi, me chamo {1}, e tenho {2}anos de idade. Trabalho como {3} e estou aprendendo a linguagem {4}.".format(nome, idade, profissao, linguagem))

# Método de variáveis nomeadas

print("Oi, me chamo {nome}, tenho {idade} anos de idade, trabalho como {profissao}, e estudo a linguagem {}")

