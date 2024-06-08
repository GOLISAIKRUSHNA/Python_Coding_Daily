
leap=int(input())
base=False
if leap%4==0:
    if leap%100==0:
        if leap%400==0:
            base=True
            exit
        else:
            base=False
            exit
    else:
            base=True
            exit
else:
    base=False

if base==True:
    print(f"leap year {leap}")
else:
    print(f"not a leap year {leap}")
