def hcf(a,b):
    if(b == 0):
        return a
    else:
        return hcf(b,a%b)

astr = input("First Num: ")
bstr = input("Second Num: ")

a = int(astr)
b = int(bstr)

print(f"HCF / GCD of {a} and {b} is " + str(hcf(b, a%b)))
