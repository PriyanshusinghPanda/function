a=int(input("enter the number:-"))
def mon(n, pss=int()):
    tem = n
    while tem>0:
        pss=pss*10+tem%10
        tem= tem//10
    return pss

b= mon(a)
print(b)
