def square_root(n):
    epsilon=0.0000001
    x=10
    while True:
        #print (x)
        y=(x+n/x)/2
        if abs(y-x)<epsilon:
            break
        x=y
    return y

def main():
    import math
    # print("So".ljust(5),"KQ_tinh".ljust(20),"KQ_thuVien".ljust(20),"Chenh_lech".ljust(20))
    print("{0:6}{1:21}{2:21}{3:21}".format("So","KQ_tinh","KQ_thuVien","Chenh_lech"))
    '''Giải thích:  ljust: Canh trái và lấy chữ thứ 2 làm mốc
                    Còn cái định dạng theo chỉ số: Lấy chữ thứ 1 làm mốc'''
    for i in range(1,10,1):
        x=square_root(i)
        y=math.sqrt(i)
        z=abs(x-y)
        print(str(float(i)).ljust(5),str(x).ljust(20),str(y).ljust(20),str(z).ljust(20))

main()