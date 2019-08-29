def mutateTheArray(n, a):
    b = []
    for i in range(n):
        b.append(getValue(a, i-1)+a[i]+getValue(a, i+1))
    return b


def getValue(array, i):
    if i < 0 or i > len(array)-1:
        return 0
    else:
        return array[i]

# ----


def alternatingSort(a):
    if len(a) != len(set(a)):
        return False
    b = sorted(a)
    l = len(a)
    right = l-1
    left = 0
    for i in range(l):
        if i % 2 == 0:
            if b[i] != a[left]:
                return False
            left += 1
        else:
            if b[i] != a[right]:
                return False
            right -= 1
    return True

# --


def meanGroups(a):
    result = []
    means = []  # contains mean each array in array
    Means = []  # contains distinct means
    for i in a:
        means.append(sum(i)/len(i))
    for i in means:
        if i not in Means:
            Means.append(i)
    for i in Means:
        temp = []
        for j in range(len(means)):
            if i == means[j]:
                temp.append(j)
        result.append(temp)
    return result

# ---


def concatenationsSum(a):
    lst = []
    for i in a:
        for j in a:
            lst.append(eval(str(i)+str(j)))
    return sum(lst)

# ---


def hashMap(queryType, query):
    dict = {}
    result = 0
    for i in range(len(queryType)):
        cmd = queryType[i]
        temp = query[i]
        if cmd == "insert":
            insert(dict, temp[0], temp[1])
        elif cmd == "get":
            result += get(dict, temp[0])
        elif cmd == "addToKey":
            dict = addToKey(dict, temp[0])
        elif cmd == "addToValue":
            addToValue(dict, temp[0])
    return result


def insert(d, x, y):  # x: y
    d[x] = y


def get(d, x):
    return d[x]


def addToKey(d, x):
    lst = {}
    for k, v in d.items():
        insert(lst, k + x, v)
    return lst


def addToValue(d, y):
    for k, v in d.items():
        d[k] += y

# --


def mergeStrings(s1, s2):
    result = ''
    i1 = 0
    i2 = 0
    while len(result) < len(s1 + s2):
        t1, t2 = get(s1, i1), get(s2, i2)
        if t2 == '' and t1 != '' or t1 != '' and t1 < t2 or t1 == t2:
            result += t1
            i1 += 1
        elif t1 == '' and t2 != '' or t2 != '' and t1 > t2:
            result += t2
            i2 += 1
    return result


def get(str, index):
    if index >= len(str):
        return ''
    else:
        return str[index]
