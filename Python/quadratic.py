

# x=-b+or-sqrt(b**2 -4ac)/2*a


def quad(a,b,c):
    
    tri=b**2-4*a*c

    x=(-b+tri**2)/2*a

    y=(-b-tri**2)/2*a

    print(f"roots x:{x},y:{y}")

            
        

a,b,c=input().split()
a=int(a)
b=int(b)

c=int(c)

quad(a,b,c)