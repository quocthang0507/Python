# Reference from https://daynhauhoc.com/t/sua-code-tao-ma-phuong-bac-le/94984/3

def KhoiTaoMaTran(n):
    return [[0 for x in range(n)] for y in range(n)]


def InMaTran(arr, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end='\t')
        print()


def XuLyMaTran(arr, n):
    i = 0
    j = int(n/2)
    for k in range(1, n*n + 1):
        arr[i][j] = k
        if i == 0 and j == n - 1:
            i += 1
            continue
        i -= 1
        j += 1
        if i < 0:
            i = n - 1
        if j > n - 1:
            j = 0
        if arr[i][j] > 0:
            i += 2
            j -= 1


if __name__ == "__main__":
    n = 0
    while n % 2 == 0:
        n = int(input('Nhap kich thuoc ma tran la mot so le: '))
    arr = KhoiTaoMaTran(n)
    XuLyMaTran(arr, n)
    InMaTran(arr, n)
