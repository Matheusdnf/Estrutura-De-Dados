v = [5, 6, 9, 8,23,232,6,26,8,4,519,49815,23,198,103,29,8150,89,150,4981520,915,20, 7]
#v=vetor
#s=inicio do array
#e=final do array
def quick_sort(v, s, e):
    if s < e:
        #irá partir o vetor
        p = partition(v, s, e)
        #percorrer o vetor a esquerda, que seria os números menores que o pivo
        quick_sort(v, s, p - 1)
        #percorrer o vetor a direita, que seria os números maiores que o pivo
        quick_sort(v, p + 1, e)

def partition(v, s, e):
    #define o pivo como o último elemento da lista
    p = e 
    #d mantém a posição do último elemento que é menor ou igual ao pivô
    d = s-1
    #irá percorer a lista para ordenar a posição do pivor , os ordenando da esquerda para a direita
    for i in range(s, e):
        if v[i] <= v[p]:
            d = d + 1
            v[i], v[d] = v[d], v[i]
    aux = v[d + 1]
    v[d + 1] = v[p]
    v[p] = aux
    return d+1

quick_sort(v, 0, len(v) - 1)
print(v)