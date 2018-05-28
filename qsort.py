array = [2,3,1,6,9,4,7,5,0,8]

def qsort(d, c):
    i = d
    j = c
    m = array[int((d+c)/2)]
    while i <= j:
        while array[i] < m: i = i + 1
        while array[j] > m: j = j - 1
        if i <= j:
            t = array[i]
            array[i] = array[j]
            array[j] = t
            i = i + 1
            j = j - 1
    if i < c: qsort(i, c)
    if j > d: qsort(d, j)

qsort(0, len(array)-1)
print (array)