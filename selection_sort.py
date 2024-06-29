v = [6,2,3,5]
# v-Vetor
# n-Quanidade de números dentro do vetor
def selection_sort(v, n):
    #é n-1 por causa que vai percorrer o array n vai precisar comparar com o último elemento
    for i in range(n-1):
        #o min serve para guardar o valor do indice do vetor
        min = i
        #o i+1 serve para ir percorrendo todo o array
        #só ira entrar nesse laço se o vetor da posição 0 for menor que o posterior
        for j in range(i+1,n):
            #para entrar no if o valor de v[j] tem que ser menor que v[min]
            if (v[j] < v[min]):
                #guardar a posição do array para poder fazer a troca
                min = j
        #armazena o valor do vetor para n perde-lo
        v[min],v[i]=v[i],v[min]
        #aux = v[i]
        #v[i] pega o ventor anterior e troca com o da frente
        #v[i] = v[min]
        #v[min] = aux

n=len(v)
selection_sort(v, n)
print(v)

