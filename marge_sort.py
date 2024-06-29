v = [5, 6, 9, 8, 7]
#v-vetor
#s-ínicio do array
#e-final do array
def merge_sort(v, s, e):
    if s < e:
        m = (s + e) // 2
        merge_sort(v, s, m)
        merge_sort(v, m + 1, e)
        merge(v, s, m, e)

def merge(v, s, m, e):
    i = s
    j = m + 1
    w = []
    for k in range(e - s + 1):
        if (i <= m) and ((j > e) or (v[i] < v[j])):
            w.append(v[i])
            i = i + 1
        else:
            w.append(v[j])
            j = j + 1
    for k in range(e - s + 1):
        v[s + k] = w[k]

merge_sort(v, 0, 5-1)
print(v)


