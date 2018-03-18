import math

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def estimate_pi():
    factor=2*math.sqrt(2)/9801
    k=0
    x=0
    while True:
        tuSo=factorial(4*k)*(1103+26390*k)
        mauSo=factorial(k)**4 * 396**(4*k)
        soHang=tuSo/mauSo
        if(soHang<1e-15):
            break
        x+=factor*soHang
        k+=1
    return 1/x
    
print(estimate_pi())