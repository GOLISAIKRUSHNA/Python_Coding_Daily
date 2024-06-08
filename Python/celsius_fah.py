

cel=int(input())

choose=input("enter the unit k or f or c")


if choose=='f':
    fah=cel*9/5 +32
    print(fah)
    exit
elif choose=="k":
    kel=cel+273
    print(kel)
    exit
else:
    print(cel)




