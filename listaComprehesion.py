#List comprehension é uma forma compacta de criar listas aplicando
#uma expressão e filtro em cada item de uma sequência, tudo numa linha só.
palavras = ["computador", "sol", "janela", "nuvem", "carro", "bicicleta", "lua"]


nova_lista = [letras for letras in palavras if len(letras) > 5 ]
print(nova_lista)



