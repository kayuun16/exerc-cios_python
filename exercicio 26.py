#  26) Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

print("Qual a quantidade atual do produto em estoque?")
qtd_atual = int(input())

print("Qual a quantidade maxima de estoque do produto?")
qtd_max = int(input())

print("Qual a quantidade minima de estoque do produto?")
qtd_min = int(input())

qtd_media = (qtd_max + qtd_min) / 2

print("Quantidade media do produto em estoque: " + str(qtd_media))

if qtd_atual >= qtd_media:
    print("Nao efetuar compra!")
else:
    print("Efetuar compra!")